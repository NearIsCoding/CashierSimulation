/** @type { HTMLCanvasElement } */

const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");

const CANVAS_WIDTH = (canvas.width = 800);
const CANVAS_HEIGHT = (canvas.height = 300);

let isRunning = false;

let frame = 1200;

class Cashier {
  constructor() {
    this.cashierImage = new Image();
    this.cashierImage.src = cashierImg;
    this.spriteWidth = 315;
    this.spriteHeight = 200;
    //Redimenzionar Imagen
    this.width = this.spriteWidth / 2.5;
    this.height = this.spriteHeight / 2.5;
    this.x = CANVAS_WIDTH - this.width;
    this.y = CANVAS_HEIGHT - this.height;
  }

  draw() {
    //ctx.strokeRect(this.x, this.y, this.width, this.height);
    ctx.drawImage(
      this.cashierImage,
      0,
      0,
      this.spriteWidth,
      this.spriteHeight,
      this.x,
      this.y,
      this.width,
      this.height
    );
  }
}

class Person {
  constructor(id, entryTime, outTime) {
    this.personId = id;
    this.personImage = new Image();
    const numberImage = Math.floor(Math.random() * 6);
    this.personImage.src = personImgs[numberImage];
    this.spriteWidth = 200;
    this.spriteHeight = 311;
    this.entryTime = entryTime;
    this.outTime = outTime;
    this.state = entryTime;
    //Redimenzionar Imagen
    this.width = this.spriteWidth / 4;
    this.height = this.spriteHeight / 4;
    // 10 es space y 126 cashier
    this.x = this.width * -1;
    this.y = CANVAS_HEIGHT - this.height;
    /*
    this.x = CANVAS_WIDTH - (this.width + 10) * (id + 1) - 126;
    this.y = CANVAS_HEIGHT - this.height;
        this.newx = Math.random() * (CANVAS_WIDTH - this.width);
        this.newy = Math.random() * (CANVAS_HEIGHT - this.height);
        this.flapSpeed = Math.floor(Math.random() * 3 + 2);
        this.interval = Math.floor(Math.random() * 200 + 50);
        */
  }

  draw() {
    //ctx.strokeRect(this.x, this.y, this.width, this.height);
    ctx.drawImage(
      this.personImage,
      0,
      0,
      this.spriteWidth,
      this.spriteHeight,
      this.x,
      this.y,
      this.width,
      this.height
    );
  }

  update() {
    if (frame == this.entryTime) {
      this.x = CANVAS_WIDTH - (this.width + 10) * (this.personId + 1) - 126;
    }
    if (frame == this.outTime) {
      for (let index = 0; index < arrayPersons.length; index++) {
        arrayPersons[index].personId = arrayPersons[index].personId - 1;
      }
      arrayPersons.splice(0, 1);
    }
  }
}

cashier = new Cashier();

function animate() {
  ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  cashier.draw();
  arrayPersons.forEach((person) => {
    person.update();
    person.draw();
    console.log(person.outTime)
  });
  if (isRunning) {
    frame += 1;
  }
  requestAnimationFrame(animate);
}

animate();
