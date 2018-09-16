import { Component } from '@angular/core';
import { ModalController, Platform, NavParams, ViewController,NavController } from 'ionic-angular';
import { DomSanitizer} from '@angular/platform-browser';
import { BadgeEarnPage } from '../badge-earn/badge-earn';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';
/**
 * Generated class for the RecipeDetailPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-recipe-detail',
  templateUrl: 'recipe-detail.html',
})
export class RecipeDetailPage {
  baseUrl ="http://localhost:5000/";
  recipeLabel;
  trustedUrl;
  score;
  image;
  secondUrl;
  constructor(public navCtrl: NavController,public platform: Platform, public params: NavParams, public viewCtrl: ViewController, private sanitizer: DomSanitizer, private http: Http) {
    this.trustedUrl = sanitizer.bypassSecurityTrustResourceUrl(this.params.get('uri'));
    this.secondUrl = sanitizer.bypassSecurityTrustResourceUrl(this.params.get('recipe_uri'));
    this.recipeLabel = this.params.get('label');
    this.score = this.params.get('score');
    this.image = this.params.get('image');
  }

  dismiss() {
    this.viewCtrl.dismiss();
  }

  select(){
    let user_id = JSON.parse(sessionStorage.getItem('uid')).id;
    let body ={
      "label": this.recipeLabel,
      "uri" : this.params.get('uri'),
      "score" : this.score,
      "recipe_image_url" : this.image
    }
    let postUrl = this.baseUrl + "users/"+user_id+"/recipes";
    this.http.post(postUrl,body).subscribe(res =>{
      console.log(res);
    })
    this.navCtrl.push(BadgeEarnPage,this.params);
  }
}
