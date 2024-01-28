import gradio as gr
from modules.extractor import extractor


import base64

# Convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_string = image_to_base64("./images/logo.png")


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

#component-12 {
    border: 2px solid #4a7bff !important;
    border-radius: 10px !important;
    background-color: #4a7bff !important;
}

#logo {
    width: 100px; /* or the size you prefer */
    height: auto;
    display: block;
    margin: 10px auto; /* centers the logo */
}
"""
def process_video(input_video):
    extracted_data = extractor(input_video)
    # Process the video as needed
    # Check if the extraction was successful and if the output data is valid
    if not extracted_data or not extracted_data["sus_file_path"]:
        # Return a message indicating no valid output was found
        error_message = "No video found."
        return None, error_message, error_message

    output_video = extracted_data["sus_file_path"]

    if not extracted_data or not extracted_data["sus_line"]:
        # Return a message indicating no valid output was found
        error_message = "There is no text found."
        return output_video, error_message, error_message

    if not extracted_data or not extracted_data["sus_words"]:
        # Return a message indicating no valid output was found
        error_message = "There is no suspect for corruption found."
        return output_video, error_message, error_message

    print(extracted_data)
    print(output_video)

    return output_video, extracted_data["text"], extracted_data["sus_line"],

# Define the Gradio interface
logo_html = f"<img id='logo' src='data:image/png;base64,{base64_string}' alt='Group Logo'/>"

demo = gr.Interface(
    fn=process_video,
    inputs=gr.Video(label="Input Video", height=300),
    outputs=[
        gr.Video(label="Processed Video", height=300),
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Group of Words")
    ],
    css=custom_css,
    title="Automative Bribe Detection Service (AB-DS)",
    description=logo_html  # Add your logo as part of the description
)


demo.launch(share=False)

# def process_video(input_video):
#     extracted_data = extractor(input_video)
#     # Process the video as needed
#     # output_video = input_video  # This is a placeholder for your processing logic
    
#     return extracted_data["sus_file_path"], extracted_data["text"], extracted_data["text"]

