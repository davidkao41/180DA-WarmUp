"""code mostly adapted from
https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar
    
def main():
    cap = cv2.VideoCapture(0)
    while(1):
        _, frame = cap.read()
        frame = frame[200:400, 200:400]
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rframe = frame.reshape((frame.shape[0] * frame.shape[1],3)) #represent as row*column,channel number
        clt = KMeans(n_clusters=3) #cluster number
        clt.fit(rframe)

        hist = find_histogram(clt)
        bar = plot_colors2(hist, clt.cluster_centers_)

        #add rectangle in the middle
        cv2.rectangle(frame, (200,200), (400,400), (255,0,0))
        cv2.imshow("hist", bar)
        cv2.imshow("frame", frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        
if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()