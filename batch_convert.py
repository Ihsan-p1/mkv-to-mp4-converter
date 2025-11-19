import ffmpeg
import os

def convert_semua_video():
    # Mengambil lokasi folder tempat skrip ini berada
    folder_sekarang = os.getcwd()
    
    # Mendapatkan daftar semua file di folder ini
    semua_file = os.listdir(folder_sekarang)

    print(f"--- Memulai Konversi di Folder: {folder_sekarang} ---")

    jumlah_sukses = 0

    for nama_file in semua_file:
        # Cek apakah file berakhiran .mkv (Case insensitive, jadi .MKV atau .mkv terbaca)
        if nama_file.lower().endswith(".mkv"):
            
            # Tentukan nama input dan nama output
            input_path = os.path.join(folder_sekarang, nama_file)
            
            # Mengubah ekstensi dari .mkv menjadi .mp4
            # Contoh: "[Zensubs]... 01.mkv" -> "[Zensubs]... 01.mp4"
            nama_output = os.path.splitext(nama_file)[0] + ".mp4"
            output_path = os.path.join(folder_sekarang, nama_output)

            print(f"\nSedang memproses: {nama_file}")

            try:
                # PROSES STREAM COPY (Tanpa ubah resolusi)
                stream = ffmpeg.input(input_path)
                stream = ffmpeg.output(stream, output_path, vcodec='copy', acodec='copy')
                
                # Jalankan (quiet=True agar log tidak terlalu berisik)
                ffmpeg.run(stream, overwrite_output=True, quiet=True)
                
                print(f"[OK] Sukses! Disimpan sebagai: {nama_output}")
                jumlah_sukses += 1

            except ffmpeg.Error as e:
                print(f"[GAGAL] Gagal memproses {nama_file}")

    print("-" * 30)
    if jumlah_sukses == 0:
        print("Tidak ada file .mkv yang ditemukan. Pastikan skrip ini satu folder dengan videonya.")
    else:
        print(f"Selesai! Total {jumlah_sukses} video berhasil dikonversi.")

# --- Eksekusi ---
if __name__ == "__main__":
    convert_semua_video()