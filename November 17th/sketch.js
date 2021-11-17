var i = 1;


function setup() { 
  createCanvas(windowWidth, windowHeight,WEBGL);
  
  // how many rows?
  console.log(data.getRowCount());
  // what are the columns?
  console.log(data.columns);

  background(10); //baackground color
  
}

    //function mousePressed() {
function draw(){

  // use the second as a timer
  frameRate(0.45)
  if (second() % 3 == 0){
    TextVibes();
    i++
    }  
  if (second() % 4 ==0){
    francophone();
    i++
  }
  if(second() % 5 == 0){
    bilingual();
    bilingual2();
    i++
  }
   
  if ( i > 2700){
    i = 1
  }
  }
  


let result;
function preload() {
  poem = loadStrings('assets/poem.txt');
  poem2 = loadStrings('assets/poem2.txt');
  poem3 = loadStrings('assets/poem3.txt');
  french = loadStrings('assets/FrenchPoem.txt')
}

function setup() {
  background(200);
  createCanvas(1200, 800);
  textSize(20)
  textFont('Georgia')
}

function TextVibes() {
  background(0)
  fill(200,80,220)
  text(random(poem), 40, 40, 80, 80);
  fill(200,90,120)
  text(random(poem2), 120, 120, 160, 160);
  fill(220,100,110)
  text(random(poem3), 200, 200, 200, 200);
  fill(80,200,220)
  text(random(poem3), 300, 300, 200, 200);
  fill(90,200,120)
  text(random(poem2), 400, 400, 160, 160);
  fill(100,220, 170)
  text(random(poem), 500, 500, 200, 200);
   fill(80,200,220)
  text(random(poem2), 600, 400, 200, 200);
  fill(90,200,120)
  text(random(poem3), 700, 300, 160, 160);
  fill(100,220, 170)
  text(random(poem), 700, 100, 200, 200);
}

 
function francophone(){

  background(0)
  fill(200,80,220)
  text(random(french), 40, 40, 80, 80);
  fill(200,90,120)
  text(random(french), 120, 120, 160, 160);
  fill(220,100,110)
  text(random(french), 220, 220, 200, 200);
  fill(80,200,220)
  text(random(french), 300, 300, 200, 200);
  fill(90,200,120)
  text(random(french), 400, 400, 160, 160);
  fill(100,220, 170)
  text(random(french), 500, 500, 200, 200);
}
 function bilingual(){
    
  background(0)
  fill(200,80,220)
  text(random(french), 40, 40, 80, 80);
  fill(200,90,120)
  text(random(poem), 120, 120, 160, 160);
  fill(220,100,110)
  text(random(poem2), 220, 220, 200, 200);
  fill(80,200,220)
  text(random(french), 300, 300, 200, 200);
  fill(90,200,120)
  text(random(french), 400, 400, 160, 160);
  fill(100,220, 170)
  text(random(poem3), 500, 500, 200, 200);
  fill("purple")
  text(random(french), 600, 400, 200, 200);
  fill("yellow")
  text(random(french), 700, 300, 160, 160);
  fill("white")
  text(random(poem), 700, 100, 200, 200);
    
  }   
  function bilingual2(){
    
  background(0)
  fill(200,80,220)
  text(random(french), 140, 40, 180, 80);
  fill(200,190,120)
  text(random(poem), 220, 720, 260, 260);
  fill(220,100,210)
  text(random(poem2), 220, 320, 200, 200);
  fill(180,200,220)
  text(random(french), 300, 300, 200, 200);
  fill(90,200,120)
  text(random(french), 700, 250, 270, 560);
  fill(100,220, 170)
  text(random(poem3), 300, 570, 400, 200);
  fill("purple")
  text(random(french), 600, 400, 200, 200);
  fill("yellow")
  text(random(french), 700, 900, 760, 160);
  fill("white")
  text(random(poem), 1000, 300, 300, 600);
    
    
  }



