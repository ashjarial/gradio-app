import gradio as gr
import pandas as pd


def relevation_metric(summary:str,transcript:str)->int:
    
    return 2;

def coherence_metric(summary:str,transcript:str)->int:
    
    return 3;

def safety_metric(summary:str,transcript:str)->int:
    
    return 5;



def fn(summary:str,transcript:str)->pd.DataFrame:
    
    relv_score=relevation_metric(summary,transcript);
    chr_score=coherence_metric(summary,transcript);
    sft_score=safety_metric(summary,transcript);
   
    
    df = pd.DataFrame({'Evaluation_metric': ['relevance', 'coherence', 'safety'], 'Score': [relv_score, chr_score, sft_score]})
    
    return df;

Interface = gr.Interface(fn=fn, 
                        inputs=[
                        gr.Textbox(label='Transcript',lines=8, placeholder="Enter your transcript"),  # Specify numerical input type
                        gr.Textbox(label='Summary',lines=8, placeholder="Enter your summary")   # Specify numerical input type
                        ],
                    outputs="dataframe",
                    allow_flagging='never',
                    title="Interview Metric Evaluation")
    
if __name__ == "__main__":
    Interface.launch()