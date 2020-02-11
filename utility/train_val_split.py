import os 
import glob
import shutil

output_="dataset"
os.makedirs(output_,exist_ok=True)


def image_move_and_txt(data,type_,root):
    # os.makedirs(type_,exist_ok=True) 
    img_path = output_+"/"+type_+"/img"
    os.makedirs(img_path,exist_ok=True)
    txt = open(output_+"/"+type_+"/gt.txt","w") 
    for i in data:
        image,label= i.split(" ")
        txt_save_image= image
        image = root+"/img/"+image
        if label == "\u200c" or label == "\u200d":
            continue
        if os.path.exists(image):
            shutil.copy(image,img_path)
            if label:
                txt.write(txt_save_image+" "+label+"\n")
            print(i)
    txt.close()



def main(data_path):
    annotation_path = data_path+"/bn_annotation.txt"
    with open(annotation_path,"r") as file_:
        data = file_.read().split("\n")
        val = int((len(data)*20)/100)
        image_move_and_txt(data[val:],"train",data_path)
        image_move_and_txt(data[:val],"val",data_path)
if __name__=="__main__":
    data_path="raw_dataset"
    main(data_path)
    
