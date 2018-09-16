import { Component } from '@angular/core';
import {ModalController,NavController, NavParams } from 'ionic-angular';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';
import { RecipeDetailPage } from '../recipe-detail/recipe-detail';
/**
 * Generated class for the SavedRecipesPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-saved-recipes',
  templateUrl: 'saved-recipes.html',
})
export class SavedRecipesPage {
  recipes =[{"recipe_name":"","recipe_image_url":""}];
  baseUrl ="http://localhost:5000/";
  constructor(public navCtrl: NavController, public navParams: NavParams, private http: Http, private modal: ModalController) {
    let user = JSON.parse(sessionStorage.getItem('uid'));
    let user_id = user.id;
    let getUrl = this.baseUrl+"users/"+user_id+"/recipes";
    http.get(getUrl).subscribe(res => {
      this.recipes = JSON.parse(res.text()).recipes;
    });
    this.recipes.splice(0,1);
  }

  view(recipe){
    this.navCtrl.push(RecipeDetailPage,recipe);
  }
}
