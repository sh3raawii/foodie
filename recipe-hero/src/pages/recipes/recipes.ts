import { Component } from '@angular/core';
import { ModalController, Platform, NavParams, ViewController, NavController } from 'ionic-angular';
import { RecipeDetailPage } from '../recipe-detail/recipe-detail';
import { DomSanitizer} from '@angular/platform-browser';

/**
 * Generated class for the RecipesPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-recipes',
  templateUrl: 'recipes.html',
})
export class RecipesPage {
  
  recipes;
  constructor(public navCtrl: NavController, public modalCtrl: ModalController, private sanitizer: DomSanitizer, private params: NavParams) {
    this.recipes = this.params.get('recipes');
  }

  openModal(recipe) {
    this.navCtrl.push(RecipeDetailPage,recipe);
  }

}
