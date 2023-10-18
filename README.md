# Python-Language-Translator-Using-Tkinter-gTTS-and-googletrans
In our increasingly interconnected world, the ability to cross linguistic barriers is more important than ever. As a Social Media Marketer, I had the opportunity to work for an e-commerce firm in the Philippines and was expected to always translate my posts from English to Tagalog. As such, picture being able to interact freely with persons from various language origins.

There are numerous approaches to language translation, and deep learning engineers have done exceptionally well in this subject. However, in this article, I will teach you how to create a basic yet powerful language translator. I will use three generally accessible tools such as Tkinter, Google Trans, and gTTS (Google Text-to-Speech). Let us get started without any further hesitation. Also, in this article, we will be using user-friendly IDEs like PyCharm, Jupyter Notebook, Sublime Text, Thonny, or VSCode. These integrated development environments offer intuitive interfaces, helpful debugging tools, and built-in support for Python libraries.

Please Note: This article is for intermediate and expert Python developers conversant with functions, conditional flow, and terminologies. However, I am open to questions and guidance for all newbie who may have the context and is finding the process difficult.

**Installation of Libraries**

Tkinter is a strong and widely used Python framework designed to create beautiful graphical user interfaces (GUIs). It's extremely easy to use and helps Python developers to create interactive and eye-catching applications. Tkinter makes it easier to create windows, buttons, menus, and other GUI elements in Python. To install Tkinter, you must first have Python installed on your machine, as Tkinter comes integrated with Python versions 3.1 and above. If not, use Python's package manager, pip, to install it in your IDE terminal with the command:

![](https://lh7-us.googleusercontent.com/jjWrCD9YLSSQaXdFcvb1V4LvPGalw_L_JcHLeXhr4-EKnh3B777eIU8uWYYdWmxnKvrBCT6VgViG6TvoCUDMXVVDX75heMuuPrq5WlPOX26-RTYRtqNIANZdTWhSjUlJWJ8tXrz6XuRm-ZoF2FO3Tew)

However, in a situation where you are using Python 3.0 above, instead of installing, all you have to do is import tkinter

![](https://lh7-us.googleusercontent.com/zcPHyvYQgESBng2olZX7gqiHVKGFOxFucoHq4hwjvwYKJhfEqL6jIjLclXAftuI7dbWWdoml8-Pu6_dcQ1jtIP889FGW9VsA09E_LT6XX-3mAHbJilYymlj7VMrnVC8qGYw9sEFJ9aNbr6PMevB249Y)

"googletrans" is the next library to be installed for this project. This is a Python programming framework for Google Translate that allows developers to smoothly add language translation features to their applications. It's a wonderful tool for projects that require multilingual assistance or global communication. You can install googletrans in your terminal using the "pip" command  just as demonstrated below:

![](https://lh7-us.googleusercontent.com/csQkKexMnefsr5JBrXZzGcGX6Mr71-GDFajM8U6jkLYvExMIdglXCPhBvgRwqSfVlA9MikncReeY8FE5STpjGfP8__kZb0J9wRM6SKCldmd3mqofIjqyuSzPupvanwDzqWr763n_pdDQv-nlAPK1UYY)

The last and final package I'll install for this project is gTTS, which stands for Google Text-to-Speech. The gTTS is a Python library and command-line interface for interacting with Google Translate's text-to-speech API. This library converts text into natural-sounding speech, allowing for cross-language applications such as language learning tools and accessibility features. To install this library, run the line of code below:

![](https://lh7-us.googleusercontent.com/hUxJ_gailsmcg4qGmP0g6TQkBFx8ELEovDlvJwz7wkYk10rRRCdvr7vem2JKlFUENS19UlDyCp0F5e1rDJ0rb0ypEsN7FqwyN8KzsgQfuKnYwpkl2zqkqrFK3uaEX0kp3Sk-p2C_XLPHMi8k8uAx_Dg)

Hurray!! You have successfully installed all the packages needed for this tutorial. In case you encounter any error using the pip command, you can use the *python -m pip install* command instead. If you are using Jupyternote book IDE, don’t panic; the process is the same.

What next? Import these libraries and get started with the main process of building your chat translator. I would have loved a step-by-step tutorial where I am able to guide you through all the stages. However, you will enjoy the article and my code methodology. All you have to do is read the comments! 

![](https://lh7-us.googleusercontent.com/4Iv79pQjRdxTVuuFQ7fJ28MeqjPc7s5zCZYdwAcPPC3b6GVnJbTsL8ibUY19sFYRwMJrFywWUcQ78X0thlvaYQ3yxoYBBbiRVG-pceXkyzWqaGDCP69SOHIzxEhX-NMb8hJzXro6Z58tNHekw_umJMA)

Congratulations! You just imported your libraries, defined your function, and stated the conditions of the translation. When you execute this code, you will see an orange and squared tkinter window ready for a more colorful impact. You can go ahead to add as many languages as you want but make sure it is included in the “googletrans” documentation. You may check out the documentation [here](https://readthedocs.org/projects/py-googletrans/downloads/pdf/latest/) to learn more.

What next? If I may ask, what are some features of a language translator app if you’ve used one? Maybe a text frame where you can enter the text you would love to translate, a button that will execute the “translate” command, and a place where the translated text will be displayed. That is beautiful. In this language translator, we already included options for five (5) languages. So what changes? Absolutely nothing in the process but we will create a dropdown frame where users can select the language they want their text translated to and then colorful formatting using tkinter functionalities.

![](https://lh7-us.googleusercontent.com/c-gho1fjSYfFDBivs9yhxtL9r5qPduGbnSe4K0BiJqmDrEPVNYy2sMRIVByNURxZ2oKYctvmo8qzTi5dO72U1Jtz5x7XLPz2CJEiiAsupVnf3JLypRseQsBskfLmgUiZDhUrADvhjXhEp6QcHCbktFQ)

You'll notice the gorgeous tkinter magic pop up on your screen as soon as you execute this code which has been wonderfully designed with Tkinter. You will further see a frame where you can enter text. After you've entered your text, click the translate button and you'll be glad you did. Now, hit the translate button!! What did you see? 

  

![](https://lh7-us.googleusercontent.com/_ASG12bNcFxl0-WyL5i31i9xbL9XRjGhk84ztKktXbi2cZ2ZOWg2DPDjKLXRFTLv_9I9TiepV61scinJ9wYoKIbASEyOMlLZiro-WVMKzSsgkZWkElQBiQT5s1I54iossN1Yrm5MMJw7fnQ5bzs3ep0)

  

You can also format your code as much as you want according to your preferences.

  

Have fun translating!!!
