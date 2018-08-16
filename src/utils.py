from shutil import copyfile, rmtree
import matplotlib.pyplot as plt
import os


def data_directories(training_list, validation_list, img_dir):
    """
    because we are using the Keras DataGenerator, we want the images used for training
    to be split in the label's directories, i.e. all images with luminosity = 1
    go into directory /1 etc ...
    :param training_list: DataFrame containing the list of files to be used for training,
    'filename' for image name and 'value' for the label.
    :param validation_list: DataFrame containing the list of files to be used for validation,
    'filename' for image name and 'value' for the label.
    :param img_dir: string, path to the directory containing the images.
    :return: None
    """
    # split files into respective directories
    if os.path.exists(img_dir+'train/0'):
        for dir in ['train', 'test']:
            for i in [0,1,2]:
                rmtree(img_dir+'{}/{}'.format(dir, str(i)))

    os.makedirs(img_dir+'train/0')
    os.makedirs(img_dir+'train/1')
    os.makedirs(img_dir+'train/2')
    for i, row in training_list.iterrows():

        copyfile(img_dir+'images/{}'.format(row['filename']),
                 img_dir+'train/{}/{}'.format(row['value'], row['filename']))

    os.makedirs(img_dir+'test/0')
    os.makedirs(img_dir+'test/1')
    os.makedirs(img_dir+'test/2')
    for i, row in validation_list.iterrows():

        copyfile(img_dir+'images/{}'.format(row['filename']),
                 img_dir+'test/{}/{}'.format(row['value'], row['filename']))

    return 'directories for classification ready.'


# save training history --------------------------------
def save_history_plot(history, path):
    """
    Save trining history plot to file.
    """
    plt.switch_backend('agg')
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('acc')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(path)
    return