import ffmpeg
import os

def convert_video_pisah_subtitle():
    folder_sekarang = os.getcwd()
    semua_file = os.listdir(folder_sekarang)

    print(f"--- Mode: Ekstrak Subtitle ke SRT & Video ke MP4 ---")
    print(f"Lokasi: {folder_sekarang}")
    
    jumlah_sukses = 0

    for nama_file in semua_file:
        if nama_file.lower().endswith(".mkv"):
            
            input_path = os.path.join(folder_sekarang, nama_file)
            
            # Nama file output (tanpa ekstensi)
            nama_dasar = os.path.splitext(nama_file)[0]
            
            output_mp4 = os.path.join(folder_sekarang, nama_dasar + ".mp4")
            output_srt = os.path.join(folder_sekarang, nama_dasar + ".srt")

            print(f"\nSedang memproses: {nama_file}")

            try:
                in_file = ffmpeg.input(input_path)

                # Output 1: Video & Audio saja ke MP4 (Copy quality)
                # 'sn': None artinya "No Subtitle" di dalam MP4-nya (supaya tidak error/konflik)
                video_stream = in_file.output(output_mp4, vcodec='copy', acodec='copy', **{'sn': None})

                # Output 2: Ambil Subtitle, ubah jadi SRT
                # Kita memaksa subtitle stream pertama (biasanya dialog) jadi srt
                sub_stream = in_file.output(output_srt, scodec='srt')

                # Jalankan keduanya sekaligus
                ffmpeg.merge_outputs(video_stream, sub_stream).run(overwrite_output=True, quiet=True)
                
                print(f"✅ Sukses!")
                print(f"   -> Video: {nama_dasar}.mp4")
                print(f"   -> Subs : {nama_dasar}.srt")
                jumlah_sukses += 1

            except ffmpeg.Error as e:
                print(f"❌ Gagal pada file ini. Mungkin tidak ada subtitle di dalamnya?")
                # print(e.stderr.decode('utf8')) # Uncomment untuk debug

    print("-" * 30)
    print(f"Selesai! {jumlah_sukses} episode berhasil diproses.")

if __name__ == "__main__":
    convert_video_pisah_subtitle()
    input("\nTekan Enter untuk keluar...")