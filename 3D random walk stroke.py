import peasy.*;
PeasyCam cam;
float rot;
float x=0, y=0, z=0;
ArrayList<PVector> points = new ArrayList<PVector>():

voiid setup(){
    size(500, 500, P3D);
    cam = new PeasyCam(This, 500);
    background(255);
}

void draw(){

    if(!mousePressed){
        rot +=.003;
    }
    rotateX(rot);
    rotateZ(rot/2);
    background(0);
    stroke( 0, 255, 255);
    strokeWeight(2);
    points.add(new PVector( x, y, z));
    for(PVector v: points){
        point( v.x, v.y, v.z);
    }

    x = x + random(-5,5);
    y = y + random(-5,5);
    z = z + random(-5,5);
    strokeWeight(5);
    stroke(255);
    point(x,y,z);
    if(X>400){
        x = -400;
    }
    if(X<-400){
        x = 400;
    }
    if(y>400){
        y = -400;
    }
    if(y<-400){
        y = 400;
    }
    if(z>400){
        z = -400;
    }
    if(z<-400){
        z = 400;
    }
    translate(0,0,0);
    noFill();
    box(800);
    


}