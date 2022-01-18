import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
// Materials
import { MatCardModule } from '@angular/material/card';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MatCardModule
  ],
  exports: [
    MatCardModule
  ]
})
export class SharedModule { }
