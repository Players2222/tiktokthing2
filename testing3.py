import time
import asyncio
import edge_tts
from rvc.infer.infer import VoiceConverter
filename="testing3.py"

script_file=__file__+"/script"
video_file=__file__+"/video"
finish_file=__file__+"/finished"

basepath=__file__.replace("\\","/").replace(filename,"/")
script_file=script_file.replace("\\","/").replace(filename,"/")
video_file=video_file.replace("\\","/").replace(filename,"/")
finish_file=finish_file.replace("\\","/").replace(filename,"/")


#tts settings
input_text = script_file+"/script.txt"
text = ""
speaker = "en-US-AndrewNeural"
rate = 0
#infer settings
pth_path = basepath+"/logs/obama/obamapath.pth"
index_path = basepath+"/logs/obama/obamaindex.index"
input_path = basepath+"/assets/audios/tts_output.wav"
output_path = finish_file+"/tts.wav"

pitch = 0
filter_radius = 3
index_rate = 0.75
volume_envelope = 1
protect = 0.5
hop_length = 128
f0_method = "rmvpe"
split_audio = False
f0_autotune = False
clean_audio = True
clean_strength = 0.5
export_format = "MP3"
upscale_audio = True
f0_file = None
embedder_model = "contentvec"
embedder_model_custom = None

async def main(text):
    rates = f"+{rate}%" if rate >= 0 else f"{rate}%"
    start_time1 = time.time()
    await edge_tts.Communicate(
        text,
        speaker,
        rate=rates,
    ).save(input_path)
    elapsed_time = time.time() - start_time1
    print(f"TTS gen time in {elapsed_time:.2f} seconds.")

class hello():
    def __init__(self):
        super().__init__()
        self.voiceover()

    def voiceover(self):
        with open(input_text, 'r') as file:
            text = file.read()
        
        asyncio.run(main(text))
        start_time1 = time.time()
        infer_pipeline = VoiceConverter()
        infer_pipeline.convert_audio(
            pitch=pitch,
            filter_radius=filter_radius,
            index_rate=index_rate,
            volume_envelope=volume_envelope,
            protect=protect,
            hop_length=hop_length,
            f0_method=f0_method,
            audio_input_path=input_path,
            audio_output_path=output_path,
            model_path=pth_path,
            index_path=index_path,
            split_audio=split_audio,
            f0_autotune=f0_autotune,
            clean_audio=clean_audio,
            clean_strength=clean_strength,
            export_format=export_format,
            upscale_audio=upscale_audio,
            f0_file=f0_file,
            embedder_model=embedder_model,
            embedder_model_custom=embedder_model_custom,
        )
        elapsed_time = time.time() - start_time1
        print(f"Inference time in {elapsed_time:.2f} seconds.")
    

if __name__ == "__main__":
    hello()