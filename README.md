# How to Use RP2040 OpenAI Example

<p align="center"><img src="https://github.com/scarletwiz/RP2040-OpenAI-Micropython/blob/main/static/images/cover_image.png"></p>


## Step 1: Prepare Software

1. The following Python IDE program is required for test, download and install from below links.

> [**Thonny**][link-thonny]

2. Deploying firmware to the device. you can use the below firmware.

> [**FW for RP2040_OpenAI_Micropython**][link-upython_fw]

If you need a detailed explanation of firmware and Thonny setup, please refer to the video below.

> [**Raspberry Pi Pico MicroPython Guide**][link-upython_gettingstart]

## Step 2: Prepare hardware

1. Combine WIZnet Ethernet HAT with Raspberry Pi Pico.
2. Connect ethernet cable to Ethernet HAT ethernet port.
3. Connect Raspberry Pi Pico to desktop or laptop using 5 pin micro USB cable.


If you use W5100S-EVB-Pico, you can skip '1. Combine...'



## Step 3: Setup Example

To test the **Open AI example**, minor settings shall be done in code.

1. Check COMport in **Device Manager** and then open **Thonny** Python IDE.

<p align="center"><img src="https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/Thonny_conf_1.png"></p>

2. Setup SPI and Reset pin in **chat_with_openai.py** or **send_prompt.py** file.

If you are not using the WIZnet PICO Board, please adjust the SPI pin configuration according to your hardware setup.

```python
spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
```

3. Enter OpenAI information(version, API key) into the **chatGPT.py** file. 

> If you have not generated an API key, please generate one on the following site
> https://platform.openai.com/account/api-keys

```python
    api_key = "insert your API-KEY"
    chatgpt_url = "https://api.openai.com/v1/chat/completions"
    chatgpt_ver= "gpt-3.5-turbo"
```

## Step 4: Upload and Run

### 1. send prompt to openAI

<p align="center"><img src="https://github.com/scarletwiz/RP2040-OpenAI-Micropython/blob/main/static/images/send_prompt.png"></p>

The function **'send_prompt_to_chatGPT'** sends the prompt to openAI and receives a response from the model. If the response is successful, the generated text is printed serial program.

Enter the prompt as a parameter for the **[send_prompt_to_chatGPT]** function.

```python
    send_prompt_to_chatGPT("Hello")

```

### 2. chat with openAI

<p align="center"><img src="https://github.com/scarletwiz/RP2040-OpenAI-Micropython/blob/main/static/images/chat_with_openAI.png"></p>

The function **'chat_with_chatGPT'** enables communication with the chatGPT model using the OpenAI API via a serial program. It user enter a message and sends it to OpenAI as a prompt, then prints the response. 

The default exit command is **">exit"**. To modify the exit command, please modify the relevant section in the **chatGPT.py** file.

```python
    end_command= ">exit"

```


<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-upython_fw]: https://github.com/scarletwiz/RP2040-OpenAI-Micropython/releases/tag/uf2_ver_1
[link-upython_gettingstart]: https://www.youtube.com/watch?v=8FcFhZRNNxE 
[link-request_lib]: https://github.com/scarletwiz/RP2040-OpenAI-Micropython/blob/main/lib/urequests.py