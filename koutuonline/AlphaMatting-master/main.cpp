/*本程序用于提取图像的前景轮廓。本项目组的工作是将原先的OpenCV 1.X代码修改为OpenCV 2.X代码。
 * 代码在WIN7 + Qt5.2.0 + OpenCV2.4.8平台上测试，成功运行。
 * Tips: input文件夹、trimap文件夹与result文件夹放在程序运行的当前目录下，即可正常运行，产生结果。
 * 2014年1月7日
*/
#include <string>
#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <cmath>
#include <vector>
#include <sharedmatting.h>
//#include <cv.h>
//#include <highgui.h>

using namespace std;

int main(int argc,char *argv[])
{
    char fileAddr[64] = {0};
    for (int n = 1; n < 2; ++n) {
        SharedMatting sm;

        sm.loadImage(argv[1]);
        sm.loadTrimap(argv[2]);
        sm.solveAlpha();
        sm.save(argv[3]);
    }

    return 0;
}
