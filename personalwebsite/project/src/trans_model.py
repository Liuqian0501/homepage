import numpy as np
import tensorflow as tf
from .transform_net import net
import io
from PIL import Image, ImageOps
import os



class TransGraph():
    """  Importing and running isolated TF graph """
    def __init__(self, img_in, checkpoint_dir):
        img = get_rgb_np(img_in) 
        img_shape = get_img(img).shape
        batch_shape = (1,) + img_shape

        self.X = np.zeros(batch_shape, dtype=np.float32)
        self.X[0] = img

        # Create local graph and use it in the session
        self.graph = tf.Graph()

        soft_config = tf.ConfigProto(allow_soft_placement=True)
        config_mu =tf.ConfigProto(intra_op_parallelism_threads=16)

        self.sess = tf.Session(graph=self.graph, config=config_mu)
        with self.graph.as_default():
            self.img_placeholder = tf.placeholder(tf.float32, shape=batch_shape,
                                            name='img_placeholder')
            self.preds = net(self.img_placeholder)

            saver = tf.train.Saver()
            # # Load 
            checkpoint_dir = os.path.dirname(os.path.abspath(__file__)) + "/Model/" + checkpoint_dir
            
            saver.restore(self.sess, checkpoint_dir)


    def run(self):
        """ Running the activation function previously imported """
        # The 'x' corresponds to name of input placeholder

        _preds = self.sess.run(self.preds, feed_dict={self.img_placeholder:self.X})
        img_np = np.clip(_preds[0], 0, 255).astype(np.uint8)
        img_out = Image.fromarray(img_np)
        
        return img_out
      
      


## need 3 dims img
def get_img(src, img_size=False):
   img = src  # Already pill image
   if not (len(img.shape) == 3 and img.shape[2] == 3):
       img = np.dstack((img,img,img))
 
   return img

## get 3d, np and rgb img
def get_rgb_np(img_in):
    img = Image.open(img_in).convert('RGB')
    img = ImageOps.fit(img, (600, 600), Image.ANTIALIAS)
    img_np = np.array(img)
    return get_img(img_np)

