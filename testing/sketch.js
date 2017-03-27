var cores = [];

function setup() {
  createCanvas(600, 300); 
  background(255);
  rectMode(CENTER);
  cores = [6];
  for (var i = 0; i < 6; i++) { 
    cores[i] = random(0, 255);
  }
  
} 

function draw() {
noStroke();
  fill(cores[0], cores[1], cores[2]);
  rect(width/4, height/2, width/2, height);
  
  fill(cores[3], cores[4], cores[5]);
  rect(width/4, height/2, width/10, height/5);
  rect(width/4+width/2, height/2, width/2, height); 
  
  fill(cores[0], cores[1], cores[2]);
  rect(width/4+width/2, height/2, width/10, height/5);
}

function keyPressed(){
  cores = [6];
  for (var i = 0; i < 6; i++) { 
    cores[i] = random(0, 255);
  }
}
