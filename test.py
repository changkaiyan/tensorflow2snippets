class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()
    self.dense1 = tf.keras.layers.[Dense Like Layer]

  def call(self, inputs):
    x = self.dense1(inputs)
    return x