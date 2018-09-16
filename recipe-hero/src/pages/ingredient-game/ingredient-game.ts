import { Component } from '@angular/core';
import { NavController, NavParams} from 'ionic-angular';
import { RecipesPage } from '../recipes/recipes';
import { DomSanitizer} from '@angular/platform-browser';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';

/**
 * Generated class for the IngredientGamePage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-ingredient-game',
  templateUrl: 'ingredient-game.html',
})
export class IngredientGamePage {
  index: number;
  currentItem;
  ingredient_label;
  ingredient_details;
  ingredient_url;
  ingredients;
  selected_ingredients;
  baseUrl ="http://localhost:5000/";
  constructor(public navCtrl: NavController,private sanitizer: DomSanitizer, private params: NavParams, private http: Http) {
    this.index = 0;
    this.selected_ingredients = [];
    this.ingredients = this.params.get('ingredients');
    this.currentItem = this.ingredients[0];
    this.ingredient_url = this.sanitizer.bypassSecurityTrustResourceUrl(this.currentItem.image);
    
  }

  select(){
    if (this.selected_ingredients.length >= 2){
      let postUrl = this.baseUrl + "recipes";
      let body = {"ingredients":this.selected_ingredients};
      console.log(body);
      alert("You chose 3 ingredients");
      this.http.post(postUrl,body).subscribe(res => {
        if (res.status == 200){
          let recipes = JSON.parse(res.text());
          console.log(recipes);
          this.navCtrl.push(RecipesPage,recipes);
        }
      });
    }
    this.selected_ingredients.push(this.currentItem.name);
    this.nextItem();
  }

  nextItem(){
    if (this.index >= 44){
      this.index = 0;
    }
    this.currentItem = this.ingredients[this.index];
    this.ingredient_url = this.sanitizer.bypassSecurityTrustResourceUrl(this.currentItem.image);
    this.index++;
  }

  start(){
    let getUrl = this.baseUrl + "ingredients";
    this.http.get(getUrl).subscribe(res => {
      console.log(res);
      let ingredients = JSON.parse(res.text());
      this.ingredients = ingredients.ingredients;
      this.currentItem = this.ingredients[0];
      this.ingredient_url = this.sanitizer.bypassSecurityTrustResourceUrl(this.currentItem.image);
    });
  }

}
