const { createCanvas } = require('canvas');
const fs = require('fs');

// 出力する文字
const text = "こんにちは、世界！";

console.log('画像を保存しました: output.png');
// キャンバスの設定
const fontSize = 40;
const canvas = createCanvas(500, 100); // キャンバスサイズを指定
const ctx = canvas.getContext('2d');

// 背景を白に設定
ctx.fillStyle = 'white';
ctx.fillRect(0, 0, canvas.width, canvas.height);

// フォントと文字色を設定
ctx.font = `${fontSize}px Arial`;
ctx.fillStyle = 'black';

// 文字を描画
ctx.fillText(text, 10, 50);

// 画像を保存
const buffer = canvas.toBuffer('image/png');
fs.writeFileSync('output.png', buffer);
console.log('画像を保存しました: output.png');
