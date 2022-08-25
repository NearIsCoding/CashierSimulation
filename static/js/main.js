/** @type { HTMLCanvasElement } */

const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");

const CANVAS_WIDTH = (canvas.width = 800);
const CANVAS_HEIGHT = (canvas.height = 300);

let isRunning = false;

let frame = 0;
let delay = 0;

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
    if (frame == parseInt(this.entryTime)) {
      queue.push(this);
      this.x = CANVAS_WIDTH - (this.width + 10) * queue.length - 126;
    }
    if (frame == parseInt(this.outTime)) {
      console.log("Person out: ", this.personId);
      let removeIndex = null;
      for (let index = 0; index < queue.length; index++) {
        if (queue[index].personId == this.personId) {
          removeIndex = index;
          break;
        }
      }
      queue.splice(removeIndex, 1);
      console.log("People: ", queue.length);
    }
    for (let index = 0; index < queue.length; index++) {
      if (queue[index].personId == this.personId) {
        this.x = CANVAS_WIDTH - (this.width + 10) * (index + 1) - 126;
        break;
      }
    }
  }
}

cashier = new Cashier();

function animate() {
  ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  cashier.draw();
  arrayPersons.forEach((person) => {
    person.update();
  });
  queue.forEach((person) => {
    person.draw();
  });
  if (isRunning) {
    if (delay >= 2) {
      frame += 1;
      delay = 0;
    } else {
      delay += 1;
    }
  }
  requestAnimationFrame(animate);
}

animate();
