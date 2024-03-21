#coding = 'utf-8'
import sys
import json
import threading
import cv2

class CvHelper:

    def __init__(self):
        pass

    def DrawCircleAsync(self,mat, p,radius):
        th = threading(target=self.DrawCircle, args=[mat, p,radius])
        th.start()
        pass

    def DrawCircle(self,mat, p,radius):
        ssd_h, ssd_w, _ = mat.shape
        cv2.circle(mat, p, radius, (0, 255, 0), -1)
        pass

    def DrawCircle2(self,mat, p,radius):
        ssd_h, ssd_w, _ = mat.shape
        cv2.circle(mat, p, radius, (255, 255, 255), -1)
        pass

    def PutTextAsync(self,mat, text, p,fs,tn):
        th = threading(target=self.PutText, args=[mat, text, p,fs,tn])
        th.start()
        pass

    def PutText(self,mat, text, p,fs,tn):
        ssd_h, ssd_w, _ = mat.shape
        cv2.putText(mat, text, p, cv2.FONT_HERSHEY_SIMPLEX, fs, (0, 255, 0), tn)
        pass
    
    def ImWriteAsync(self, mat, filepath):
        th = threading(target=self.ImWrite, args=[mat, filepath])
        th.start()

    def ImWrite(self, mat, filepath):
        cv2.imwrite(filepath, mat)
        pass
