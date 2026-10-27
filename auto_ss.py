import os
import asyncio
import argparse
import http.server
import socketserver
import threading
from pathlib import Path
from playwright.async_api import async_playwright

# Konfigurasi Port untuk Server Lokal Sementara
PORT = 8080

def start_local_server(folder_path):
    """Menjalankan server HTTP lokal di background supaya mirip Live Server"""
    os.chdir(folder_path)
    handler = http.server.SimpleHTTPRequestHandler
    handler.log_message = lambda *args: None  # Matikan log terminal supaya bersih
    
    httpd = socketserver.TCPServer(("", PORT), handler)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    return httpd

def get_default_output_path(subfolder_name="Hasil_Laporan_Tugas"):
    """Otomatis simpan folder output di Desktop pengguna (fallback ke Documents)"""
    desktop_path = Path.home() / "Desktop"
    if not desktop_path.exists():
        desktop_path = Path.home() / "Documents"
    return desktop_path / subfolder_name

async def capture_html_as_output(folder_path, output_dir):
    """Mode 1: Screenshot output web menggunakan server lokal"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"[!] Folder sumber '{folder_path}' belum ada. Gua udah buatin! Masukin file HTML ke situ ya.")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    html_files = [f for f in os.listdir(folder_path) if f.endswith('.html') or f.endswith('.htm')]
    if not html_files:
        print(f"[-] Nggak ada file HTML di dalam folder '{folder_path}'")
        return

    print(f"[*] Menyalakan server lokal (Live Server simulation)...")
    server = start_local_server(folder_path)

    print(f"[*] [Mode: Output Web] Memproses {len(html_files)} file...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        for filename in html_files:
            file_url = f"http://localhost:{PORT}/{filename}"
            output_image_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")

            try:
                await page.goto(file_url, wait_until="networkidle")
                await page.screenshot(path=output_image_path, full_page=True)
                print(f"[+] Output Web: {filename} -> tersimpan.")
            except Exception as e:
                print(f"[-] Gagal {filename}: {str(e)}")

        await browser.close()
    
    server.shutdown()
    print(f"\n[✨] Beres! Cek Desktop lu, foldernya ada di:\n📁 {output_dir}")

def capture_code_snippets(folder_path, output_dir):
    """Mode 2: Merangkum kodenya ke file Markdown siap pakai"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"[!] Folder sumber '{folder_path}' belum ada. Gua udah buatin!")
        return

    os.makedirs(output_dir, exist_ok=True)
    html_files = [f for f in os.listdir(folder_path) if f.endswith('.html') or f.endswith('.htm') or f.endswith('.php')]
    
    if not html_files:
        print(f"[-] Nggak ada file kode di dalam folder '{folder_path}'")
        return

    print(f"[*] [Mode: Source Code] Merangkum {len(html_files)} file kode...")

    output_md = os.path.join(output_dir, "laporan_source_code.md")
    with open(output_md, 'w', encoding='utf-8') as outfile:
        outfile.write("# Laporan Source Code Tugas\n\n")
        
        for filename in html_files:
            file_path = os.path.join(folder_path, filename)
            outfile.write(f"## File: `{filename}`\n\n```html\n")
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
            except Exception as e:
                outfile.write(f"// Error baca file: {str(e)}")
            outfile.write("\n```\n\n---\n\n")

    print(f"\n[✨] Beres! Cek Desktop lu, file rangkuman tersimpan di:\n📁 {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool Auto-Screenshot Tugas HTML & Kode")
    parser.add_argument("--mode", choices=["output", "kode"], default="output", 
                        help="Pilih mode: 'output' buat screenshot tampilan web, atau 'kode' buat ambil kodenya.")
    parser.add_argument("--folder", default="desain", help="Nama folder sumber (default: desain)")

    args = parser.parse_args()
    destination_folder = get_default_output_path("Hasil_Laporan_Tugas")

    if args.mode == "output":
        asyncio.run(capture_html_as_output(args.folder, destination_folder))
    elif args.mode == "kode":
        capture_code_snippets(args.folder, destination_folder)