from django.shortcuts import render
from .forms import Pictureform
import dlib
from skimage import io
from scipy.spatial import distance

def index(request):
    return render(request, 'vid4/homePage.html')
def contact(request):
    facerec = dlib.face_recognition_model_v1('vid4/static/dlib/dlib_face_recognition_resnet_model_v1.dat')
    sp = dlib.shape_predictor('vid4/static/shape/shape_predictor_68_face_landmarks.dat')
    detector = dlib.get_frontal_face_detector()
    img = io.imread('vid4/static/vid4/image/roman.jpg')
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        shape = sp(img, d)
    face_descriptor1 = facerec.compute_face_descriptor(img, shape)
    img = io.imread('vid4/static/vid4/image/1.jpg')
    dets_webcam = detector(img, 1)
    for k, d in enumerate(dets_webcam):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        shape = sp(img, d)
    face_descriptor2 = facerec.compute_face_descriptor(img, shape)
    a = distance.euclidean(face_descriptor1, face_descriptor2)
    print(a)
    x = 0.5;
    return render(request, 'vid4/basic.html', {'a': a,'x': x, })



def page(request):
    if request.method == 'POST':

        form = Pictureform(request.POST, request.FILES)

        if form.is_valid():

            form.save(commit=True)

    else:
        form = Pictureform()

    return render(request, "vid4/homePage.html", {'form': form})


