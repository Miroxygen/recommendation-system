/**
 * @file Defines controller for application.
 * @module controllers/controller
 * @author Miranda Holmlund
 * @version 1.0
 */

import fetch from "node-fetch"

/**
 * Controller for application.
 */
export class Controller {
  constructor() {
    this.recommendations
  }

  /**
   * Shows recommendations.
   * @param {object} req Express request object.
   * @param {object} res Express response object.
   */
  async showRecommendations(req, res) {
    const response = await fetch("http://localhost:8080/get-users")
    const users = await response.json()
    const rec = this.recommendations
    res.render('home', { users,  rec})
  }

  /**
   * Creates recommendations.
   * @param {object} req Express request object.
   * @param {object} res Express response object.
   */
  async createMovieRecommendations(req, res) {
    const movies = await this.getMovieTitles(req, res)
    const rec = await this.getRecommendationNumbers(req, res)
    const array = []
    if(rec != undefined) {
      for(let i = 0; i < rec.length; i++) {
        if(movies.hasOwnProperty(rec[i][1]).toString()) {
          array.push({title : movies[rec[i][1]][0][0], year : movies[rec[i][1]][0][1], score : rec[i][0]})
        }
      }
      this.recommendations = array
    } 
    res.redirect('.')
  }

  /**
   * Gets the titles to show them instead of ids.
   * @param {object} req Express request object.
   * @param {object} res Express response object.
   */
  async getMovieTitles(req, res) {
    const response = await fetch("http://localhost:8080/get-movies")
    const movies = await response.json()
    return movies
  }



  /**
   * Gets the score of movies.
   * @param {object} req Express request object.
   * @param {object} res Express response object.
   */
  async getRecommendationNumbers(req, res) {
    try {
      const {rectype, user, method} = req.body
      if(rectype == "itembased" && method == "pearson") {
        return
      }
      const response = await fetch("http://localhost:8080/get-rec", {
        method : 'POST',
        headers: {
          'Accept' : 'application/json',
          'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
          user : user,
          method : method,
          rectype : rectype
        })
      })
      const rec = await response.json()
      return rec
    } catch (error) {
      console.log(error)
    }

  }
}