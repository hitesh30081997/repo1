import gradio as gr
import nemo.collections.asr as nemo_asr
import os
import json
# 1. Load your local .nemo model
# Replace 'your_model.nemo' with the actual path to your file
print("Loading NeMo ASR model...")
model = nemo_asr.models.ASRModel.restore_from(restore_path="/home/common/Downloads/nvidia-conformer-large-slurp-other-default-v1/slu_conformer_transformer_large_slurp_1.nemo")

def predict_intent_and_slots(audio_path):
    if audio_path is None:
        return "Please upload or record an audio file", None
    try:
        predictions = model.predict([audio_path])
        raw_output = predictions[0] if predictions else "No Predictions Returned"
        
        try:
            parsed_json = json.loads(raw_output)
            formatted_output = json.dumps(parsed_json, indent=4)
        except Exception:
            formatted_output = raw_output
            
        return formatted_output
    except Exception as e:
        return f"An error occured during inference: {str(e)}"
    
with gr.Blocks(title="Conformer Large SLURP Demo") as demo:
    gr.Markdown("Conformer Large SLURP Demo")
    gr.Markdown(
        "This Web interface utilizes NVIDIA Nemos Conformer Large Model"
        "Trained on the SLURP dataset to perform spoken language understanding Joint Intent Classification and Slot Filling")
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone", "upload"],
                type="filepath",
                label="Input Audio (16kHz WAV Mono)")
            submit_btn = gr.Button("Analyses speech", variant="primary")
            
        with gr.Column():
            output_text = gr.Code(
                label="Extracted Semantics (Intent and Slots)",
                language="json")
    submit_btn.click(fn=predict_intent_and_slots,
                     inputs=audio_input,
                     outputs=output_text)
    
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=6000)