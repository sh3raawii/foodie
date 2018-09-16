import { Component } from '@angular/core';
import {NavController, NavParams } from 'ionic-angular';
import { DomSanitizer} from '@angular/platform-browser';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';
import { BadgeCollectionPage } from '../badge-collection/badge-collection';
import { RecipesPage } from '../recipes/recipes';
import { SavedRecipesPage } from '../saved-recipes/saved-recipes';
/**
 * Generated class for the BadgeEarnPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-badge-earn',
  templateUrl: 'badge-earn.html',
})
export class BadgeEarnPage {
  baseUrl ="http://localhost:5000/";
  stars;
  score;
  display_score = true;
  is_scored: boolean;
  scored_url;
  scored_title;
  has_badge = false;
  random_id;
  badge;
  badge_id;
  recipes;
  constructor(public navCtrl: NavController, public navParams: NavParams, private sanitizer: DomSanitizer, private http: Http) {
    this.score = this.navParams.get('score');
    let getUrl = "https://rickandmortyapi.com/api/character/";
    this.score = Math.round(this.score);
    if (this.score > 49){
      this.is_scored = true;
      this.scored_url = sanitizer.bypassSecurityTrustResourceUrl("http://www.reactiongifs.com/r/cheering_minions.gif");
      this.scored_title = "Yaaaaaaay! You got high score !!!";
      if (this.score > 75){
        this.random_id = Math.floor(Math.random() * 16) + 25;
        this.stars = Array(5).fill("star");
      } else {
        this.random_id = Math.floor(Math.random() * 14) + 13;
        this.stars = Array(4).fill("star");
      }
    }
    else{
      if (this.score > 24){
        this.random_id = Math.floor(Math.random() * 10 )+4;
        this.stars = Array(3).fill("star");
      }else{
        this.random_id = Math.floor(Math.random() * 3) + 1;
        this.stars = Array(2).fill("star");
      }
      this.is_scored = false;
      this.scored_url = sanitizer.bypassSecurityTrustResourceUrl("https://media.giphy.com/media/BEob5qwFkSJ7G/giphy.gif");
      this.scored_title = "Awwwww! Too bad! Only "+this.score;
    }
    console.log(this.random_id);
    http.get(getUrl+this.random_id).subscribe(res => {
      this.badge = JSON.parse(res.text());
      let postUrl = this.baseUrl+ "badges";
      let body = {"name" : this.badge.name,"extid":this.random_id};
      http.post(postUrl,body).subscribe(res => {
        if (res.status == 200){
          let item = JSON.parse(res.text());
          this.badge_id = item.id;
          let user = JSON.parse(sessionStorage.getItem('uid'));
          let user_id = user.id;
          let postUrl2 = this.baseUrl +"users/"+ user_id + "/badges/"+this.badge_id;
          http.post(postUrl2,null).subscribe(res => {
            console.log(res);
          });
          let getUrl2 = this.baseUrl+"users/"+user_id+"/recipes";
          http.get(getUrl).subscribe(res => {
            this.recipes = JSON.parse(res.text());
          })
          console.log(this.badge_id);
        }
      });
    });
  }

  collect(){
    this.display_score = false
    this.has_badge = true;
  }
  viewBadges(){
    this.navCtrl.push(BadgeCollectionPage);
  }

  viewRecipes(){
    this.navCtrl.push(SavedRecipesPage,this.recipes);
  }
}
