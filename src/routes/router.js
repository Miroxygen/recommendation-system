import express from 'express'
import { Controller } from '../controllers/controller.js'

export const router = express.Router()
const controller = new Controller()

router.get('/', (req, res, next) => {
  controller.showRecommendations(req, res)
})

router.post('/data', (req,res,next) => {
  controller.createMovieRecommendations(req, res)
})