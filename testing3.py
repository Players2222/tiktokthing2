from core import run_tts_script
from rvc.infer.infer import VoiceConverter
infer_pipeline = VoiceConverter()

tts_file= "C:/Users/DongYu/Desktop/things/code/python_projects/Capcut/script/script.txt",
tts_voice: str,
tts_rate: int,
pitch: int,
filter_radius: int,
index_rate: float,
volume_envelope: int,
protect: float,
hop_length: int,
f0_method: str,
output_tts_path: str,
output_rvc_path: str,
pth_path: str,
index_path: str,
split_audio: bool,
f0_autotune: bool,
f0_autotune_strength: float,
clean_audio: bool,
clean_strength: float,
export_format: str,
f0_file: str,
embedder_model: str,
embedder_model_custom: str = None,
sid: int = 0,

infer_pipeline.convert_audio(tts_file=tts_file,output_tts_path=output_tts_path,model_path=pth_path,index_path=index_path,sid=0)