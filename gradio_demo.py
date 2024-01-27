import gradio as gr
from modules.extractor import extractor


# This function takes a video file and returns the same video.
# Replace the content of this function with your video processing logic.

custom_css = """
body {
    background-color: white !important;
}
h2, label {
    color: #4a4a4a;
}
.video {
    border: 2px solid #4a7bff;
    border-radius: 10px;
}
"""

def process_video(input_video):
    extracted_data = extractor(input_video)
    # Process the video as needed
    output_video = extracted_data["sus_file_path"]  # This is a placeholder for your processing logic
    
    print(extracted_data)
    print(output_video)

    return output_video, extracted_data["sus_line"], extracted_data["sus_words"],

# Define the Gradio interface
demo = gr.Interface(
    fn=process_video,
    inputs=gr.Video(label="Input Video", height=300),
    outputs=[
        gr.Video(label="Input Video", height=300),
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Group of Words")
    ],
    css=custom_css  # Apply your custom CSS here
)# Launch the Gradio app
demo.launch()


# def process_video(input_video):
#     extracted_data = extractor(input_video)
#     # Process the video as needed
#     # output_video = input_video  # This is a placeholder for your processing logic
    
#     return extracted_data["sus_file_path"], extracted_data["text"], extracted_data["text"]

