#include "mainwindow.h"
#include <QApplication>
#include "interprete.h"
#include <iostream>
#include <ofstream>
#include <vector>

class quadtree()
{

}
class coordenadas()
{
    vector<float> coordenada;
};

class puntos{
public:
    int eti;
    vector<coordenadas> puntos;
    int etianterior;
    int age;
    puntos();
};

puntos::puntos()
{
    this->age=0;
    this->eti=0;
    this->etianterior=0;
}

class gng{
public:
    gng();
    void acercamiento(quadtree estructura);
    void puntos();
}

vector<puntos> gng::puntos(puntos tiempos,vector<puntos> myvector)
{
    myvector.pushback(tiempos);
}
void gng::acercamiento(quadtree estructura)
{
    vector<puntos> newpuntos;
    puntos mispuntos = new puntos();
    for(;;)
    {
         puntos(newpuntos,mispuntos);
    }
}

int main(int argc, char *argv[])
{
    gng final;
    vector<puntos> puntos = final.acercamiento();   
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
