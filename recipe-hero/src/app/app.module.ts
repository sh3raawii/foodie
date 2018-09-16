import { NgModule, ErrorHandler} from '@angular/core';
import { HttpModule } from '@angular/http';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';

import { AboutPage } from '../pages/about/about';
import { ContactPage } from '../pages/contact/contact';
import { HomePage } from '../pages/home/home';
import { TabsPage } from '../pages/tabs/tabs';
import { RecipesPage} from '../pages/recipes/recipes';
import {RecipeDetailPage} from '../pages/recipe-detail/recipe-detail';
import {BadgeEarnPage} from '../pages/badge-earn/badge-earn';
import {IngredientGamePage} from '../pages/ingredient-game/ingredient-game';
import {RegistrationPage} from '../pages/registration/registration';
import {BadgeCollectionPage} from '../pages/badge-collection/badge-collection';
import {SavedRecipesPage} from '../pages/saved-recipes/saved-recipes';

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

@NgModule({
  declarations: [
    MyApp,
    AboutPage,
    ContactPage,
    HomePage,
    TabsPage,
    RecipesPage,
    RecipeDetailPage,
    BadgeEarnPage,
    IngredientGamePage,
    RegistrationPage,
    BadgeCollectionPage,
    SavedRecipesPage
  ],
  imports: [
    BrowserModule,
    HttpModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    AboutPage,
    ContactPage,
    HomePage,
    TabsPage,
    RecipesPage,
    RecipeDetailPage,
    BadgeEarnPage,
    IngredientGamePage,
    RegistrationPage,
    BadgeCollectionPage,
    SavedRecipesPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
