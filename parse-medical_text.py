import gradio as gr
import os
import socks
import socket
import openai

def openai_answer(prompt):
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7890)
    socket.socket = socks.socksocket

    openai.api_key = 

    prompt = prompt

    # 调用 ChatGPT 接口
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    # 返回输入的句子
    return response

def process_prompt(text, my_tags, edit_tags):

    if edit_tags:
        my_tags.extend(";".split(edit_tags))
    ky_name = "、".join(my_tags)

    text_upper = "你是一个经验丰富的临床医师，请从[]内的病历文本{}中提取：{}的指标信息。请以json格式返回".format("["+text+"]", ky_name)
    result = openai_answer(text_upper)
    # 返回处理后的文本
    return result

def gradio():
    os.environ["http_proxy"] = ""
    os.environ["https_proxy"] = ""

    tag_default = ["T", "P", "R", "EP", "巩膜黄染", "皮肤黄染", "心率",
               "腹壁静脉曲张", "心脏听诊区杂音", "肠鸣音"]
    input_text = gr.inputs.Textbox(label="输入病历内容")
    edit_tags = gr.inputs.Textbox(label="新增指标(用英文;分隔)")


    input_tags = gr.inputs.CheckboxGroup(label="科研指标", choices=tag_default)
    output_text = gr.outputs.Textbox(label="提取科研指标")

    interface = gr.Interface(fn=process_prompt, inputs=[input_text, input_tags, edit_tags], outputs=output_text)
    interface.launch(share=True)


if __name__ == '__main__':
    gradio()

