# Tensorflow 2.0 Snippets for VS Code

<br>
<div align="center">
  <div>
    <img src="https://img.shields.io/badge/Editer-vscode-blue.svg?&style=flat-square&logo=visual-studio-code" alt="vscode" />
    <img src="https://img.shields.io/badge/build-passing-green.svg?&style=flat-square&logo=github" alt="build-passing" />
	<a href="https://github.com/changkaiyan/tensorflow2snippets">
    <img src="https://img.shields.io/badge/support-star-yello.svg?&style=flat-square&logo=github" alt="build-passing" />
	</a>
  </div>
  <div>
    <img src="https://img.shields.io/badge/Email-changkaiyan@qq.com-yello.svg?&style=flat-square" alt="email" />
    <img src="https://img.shields.io/badge/Release-v0.1-blue.svg?&style=flat-square&logo=github" alt="release" />
    
  </div>
</div>

 Type prefix `tfk:` in Python file to get start with this extension! ( `tfk` presents tensorflow keras)

 This extension includes some snippets to develop a model in your VS Code editor. It requires the minimum version of tensorflow is **2.0**. The inside **keras** package will be used in this extension. For more information, please go to [Key Features](#Key-Features) .

![ctrl](https://github.com/changkaiyan/tensorflow2snippets/raw/master/images/ctrl.gif)

## Support

While being free and open source, if you find it useful, please consider star us on the repository [tensorflow2snippets
](https://github.com/changkaiyan/tensorflow2snippets).

## Getting started

The extension requires some usefull packages, such as `tensorflow tensorflow-datasets tf-nightly`. 

<font size="4px">

~~~bash
pip install tensorflow tf-nightly 
pip install tensorflow-datasets
~~~

</font>

The visualization tool and some auxiliary tools are also important for you to train a deep learning model.

<font size="4px">

~~~bash
pip install matplotlib numpy
~~~

</font>

## Key Features

### `tfk:dataset` Field

We write some snippets to help you **load the data set easily**. But first you must import tensorflow_datasets.
~~~py
import tensorflow_datasets as tfds
~~~

~~~py
# Image Classification data set
tfk:dataset:mnist 
tfk:dataset:fmnist
tfk:dataset:cifar10 
tfk:dataset:cifar100 
tfk:dataset:imagenet2012
tfk:dataset:celeb_a 

# Object_detection data set
tfk:dataset:coco
tfk:dataset:voc2007

# Structured data set
tfk:dataset:iris

# Generative data set
tfk:dataset:cycle_gan

# Summarization data set
tfk:dataset:scientific_papers

# Text Classification data set
tfk:dataset:scicite

# Language Translate data set
tfk:dataset:flores

# Movies data set
tfk:dataset:moving_mnist

~~~

### `tfk:ctrl` Field

This field can help you control the procedure flow more convenience. They generate function like `model.fit(...)` or class like `class model(tf.keras.Model)`.

~~~py
tfk:ctrl:model
tfk:ctrl:fit
tfk:ctrl:evaluate
tfk:ctrl:compile
tfk:ctrl:callback
tfk:ctrl:saveModel
tfk:ctrl:loadModel
~~~

### `tfk:code` Field

This field can generate a runnable .py file. It can used to set the code frame. All of the codes are derived from [tensorflow official guide](https://www.tensorflow.org/tutorials). We express our appreciation for tensorflow developers and the author of the official document.

~~~py
tfk:code:mnist:simple # Simple code for img classification
tfk:code:mnist:full # More complex code for img classification
tfk:code:oxford # Code for img segmentation
tfk:code:translate # Code for NLP-translate
tfk:code:word_embeddings # Code for NLP-word embeddings
~~~

![code](https://github.com/changkaiyan/tensorflow2snippets/raw/master/images/code.gif)

## How to Contribute

This project welcomes contributions and suggestions.

Fork our [repository](https://github.com/changkaiyan/tensorflow2snippets) and you can submit the snippet you like. 

## Bug Report or Problem

If you find some bugs or have some problems on this extension. Please create your [issue](https://github.com/changkaiyan/tensorflow2snippets/issues).


## Contributors

[Kaiyan Chang](https://github.com/changkaiyan/)

## License

 <img src="https://img.shields.io/badge/LICENSE-MIT-yello.svg?&style=flat-square" alt="email" />