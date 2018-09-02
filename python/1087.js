// Dama
// Problema 1087 do URI Online Judge
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1087

const fs = require('fs')

const inputPath = process.env.input || '/dev/stdin'

const input = fs
  .readFileSync(inputPath, 'utf8')
  .split('\n')
  .slice(0, -2)
  .map(line => line
    .split(' ')
    .map(n => parseInt(n))
  )

const areEquals = ([x1, y1, x2, y2]) => (x1 === x2 && y1 === y2)

const areOnTheSameLine = ([x1, y1, x2, y2]) =>
  (x1 + y1 === x2 + y2 || x1 - y1 === x2 - y2 || x1 === x2 || y1 === y2)

const getNumOfMoves = points => areEquals(points)
  ? 0 : areOnTheSameLine(points)
  ? 1 : 2

const result = input.map(getNumOfMoves).join('\n')

console.log(result)