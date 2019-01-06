#include <iostream>
#include <opencv2/opencv.hpp>
#include <string>
#include <stdlib.h>

#define OPENCV


typedef struct {
    int w;
    int h;
    int c;
    float *data;
} image;

int windows = 0;

image make_empty_image(int w, int h, int c)
{
    image out;
    out.data = 0;
    out.h = h;
    out.w = w;
    out.c = c;
    return out;
}

image make_image(int w, int h, int c)
{
    image out = make_empty_image(w,h,c);
    out.data = (float*)calloc(h*w*c, sizeof(float));
    return out;
}
/*
void ipl_into_image(IplImage* src, image im)
{
    unsigned char *data = (unsigned char *)src->imageData;
    int h = src->height;
    int w = src->width;
    int c = src->nChannels;
    int step = src->widthStep;
    int i, j, k;

    for(i = 0; i < h; ++i){
        for(k= 0; k < c; ++k){
            for(j = 0; j < w; ++j){
                im.data[k*w*h + i*w + j] = data[i*step + j*c + k]/255.;
            }
        }
    }
}

image ipl_to_image(IplImage* src)
{
    int h = src->height;
    int w = src->width;
    int c = src->nChannels;
    image out = make_image(w, h, c);
    ipl_into_image(src, out);
    return out;
}
*/

image copy_image(image p)
{
    image copy = p;
    copy.data = (float*)calloc(p.h*p.w*p.c, sizeof(float));
    memcpy(copy.data, p.data, p.h*p.w*p.c*sizeof(float));
    return copy;
}

void constrain_image(image im)
{
    int i;
    for(i = 0; i < im.w*im.h*im.c; ++i){
        if(im.data[i] < 0) im.data[i] = 0;
        if(im.data[i] > 1) im.data[i] = 1;
    }
}

void rgbgr_image(image im)
{
    int i;
    for(i = 0; i < im.w*im.h; ++i){
        float swap = im.data[i];
        im.data[i] = im.data[i+im.w*im.h*2];
        im.data[i+im.w*im.h*2] = swap;
    }
}

static float get_pixel(image m, int x, int y, int c)
{
    assert(x < m.w && y < m.h && c < m.c);
    return m.data[c*m.h*m.w + y*m.w + x];
}

void show_image_cv(image p, const char *name, IplImage *disp)
{
    int x,y,k;
    if(p.c == 3) rgbgr_image(p);
    //normalize_image(copy);

    char buff[256];
    //sprintf(buff, "%s (%d)", name, windows);
    sprintf(buff, "%s", name);

    int step = disp->widthStep;
    cvNamedWindow(buff, CV_WINDOW_NORMAL);
    //cvMoveWindow(buff, 100*(windows%10) + 200*(windows/10), 100*(windows%10));
    ++windows;
    for(y = 0; y < p.h; ++y){
        for(x = 0; x < p.w; ++x){
            for(k= 0; k < p.c; ++k){
                disp->imageData[y*step + x*p.c + k] = (unsigned char)(get_pixel(p,x,y,k)*255);
            }
        }
    }
    if(0){
        int w = 448;
        int h = w*p.h/p.w;
        if(h > 1000){
            h = 1000;
            w = h*p.w/p.h;
        }
        IplImage *buffer = disp;
        disp = cvCreateImage(cvSize(w, h), buffer->depth, buffer->nChannels);
        cvResize(buffer, disp, CV_INTER_LINEAR);
        cvReleaseImage(&buffer);
    }
    cvShowImage(buff, disp);
}

void free_image(image m)
{
    if(m.data){
        free(m.data);
    }
}

void show_image(image p, const char *name)
{
#ifdef OPENCV
    IplImage *disp = cvCreateImage(cvSize(p.w,p.h), IPL_DEPTH_8U, p.c);
    image copy = copy_image(p);
    constrain_image(copy);
    show_image_cv(copy, name, disp);
    free_image(copy);
    cvReleaseImage(&disp);
#else
    fprintf(stderr, "Not compiled with OpenCV, saving to %s.png instead\n", name);
    save_image(p, name);
#endif
}

image ipl_to_image(IplImage* src)
{
    int h = src->height;
    int w = src->width;
    int c = src->nChannels;
    image im = make_image(w, h, c);
    unsigned char *data = (unsigned char *)src->imageData;
    int step = src->widthStep;
    int i, j, k;

    for(i = 0; i < h; ++i){
        for(k= 0; k < c; ++k){
            for(j = 0; j < w; ++j){
                im.data[k*w*h + i*w + j] = data[i*step + j*c + k]/255.;
            }
        }
    }
    return im;
}

image mat_to_image(cv::Mat m)
{
    IplImage ipl = m;
    image im = ipl_to_image(&ipl);
    rgbgr_image(im);
    return im;
}



int main() {
    std::string data_path = "/home/yl/Dataset/cat.jpeg";
    cv::Mat src = cv::imread(data_path);
    cv::imshow("Mat", src);
    image img = mat_to_image(src);
    show_image(img, "image");
    cv::waitKey(0);
    return 0;
}