import gradio as gr
from modules.extractor import extractor


# This function takes a video file and returns the same video.
# Replace the content of this function with your video processing logic.
def process_video(input_video):
    extracted_data = extractor(input_video)
    # Process the video as needed
    output_video = extracted_data["sus_file_path"]  # This is a placeholder for your processing logic
    
    return output_video

# Define the Gradio interface
demo = gr.Interface(
    fn=process_video,
    inputs=gr.Video(label="Input Video"),
    outputs=[
        gr.Video(label="Input Video"),
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Group of Words")
    ]
)
# Launch the Gradio app
demo.launch()
