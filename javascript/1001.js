// Extremamente Básico
// Problema 1001 do URI Online Judge
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1001

const fs = require('fs')

const inputPath = process.env.input || '/dev/stdin'

const [a, b] = fs
  .readFileSync(inputPath, 'utf8')
  .split('\n')
  .map(line => parseInt(line))

console.log(`X = ${a + b}`)
