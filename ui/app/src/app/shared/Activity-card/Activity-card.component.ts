import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Activity-card.component.html',
  styleUrls: ['./Activity-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Activity-card]': 'true'
  }
})

export class ActivityCardComponent {


}