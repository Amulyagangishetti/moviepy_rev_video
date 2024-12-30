import gradio as gr
from moviepy import vfx, VideoFileClip

def video_reverse(video):
    myclip=VideoFileClip(video, audio=False)
    rev_clip = myclip.with_effects([vfx.TimeMirror()])
    rev_clip.write_videofile("rev_clip.mp4")
    return "./rev_clip.mp4"
demo = gr.Interface(video_reverse,
                    gr.Video(),
                    "playable_video",
                    )

demo.launch(debug=True,share=True)
