# LLM-
基于大模型搭建可交互的医疗文本科研指标提取

对于医疗文本，病历结构化和科研指标提取，大大提高了医院对于病历数据的管理和科研的效率。病历结构化和科研指标提取借助大模型来实现，实现从病历文本→科研指标的提取，减少了代码解析的工作量，LLM可以作为医疗文本提取指标可实现的实用工具。

交互界面截图如下

![交互界面截图](https://github.com/shuyeah2356/LLM-/blob/main/imgs/1.png)

在“输入病历内容”对应的输入文本框中添加病历文本，

例如某乳腺癌病历中的体格检查文本：

体格检查：T：36.6℃ P 80次/分 R20次/分 EP 110/60mmHg。发育正常，营养中等，甚至清醒，精神欠佳，自动体位，查体合作。全身皮肤黏膜无黄染，未触及肿大淋巴结。头颅五官征程无畸形，眼睑无浮肿，巩膜无黄染，双侧瞳孔等大等圆，对光放射灵敏。耳廓无畸形，外耳道无脓血性分泌物，乳突无压痛。鼻外观无畸形，鼻通畅，鼻中隔无偏曲，鼻腔无异常分泌物，无鼻翼煽动，副鼻窦区无压痛，唇无苍白紫绡。咽部无充血，扁桃体无肿大。颈软无抵抗，颈静脉无怒张，气管居中，甲状腺未触及肿大。胸廓对称无畸形，无肋间隙增宽及变窄，双侧呼吸动度一致，听诊双飞呼吸音清，未闻及明显干湿性啰音，心前区无隆起，心界无扩大，心率80次/分，心音有力，心率整齐，心脏听诊区未闻及异常杂音。腹部隆起，无腹壁静脉曲张、未见肠型及蠕动波。未触及明显包快。肝脾肋缘未及，肠鸣音正常。肛门及外生殖器无异常。

从文本中提取如下指标：

"T", "P", "R", "EP", "巩膜黄染", "皮肤黄染", "心率", "腹壁静脉曲张", "心脏听诊区杂音", "肠鸣音"
