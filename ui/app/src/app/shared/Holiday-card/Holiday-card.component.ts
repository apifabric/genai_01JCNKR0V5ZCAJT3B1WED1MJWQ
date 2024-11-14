import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Holiday-card.component.html',
  styleUrls: ['./Holiday-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Holiday-card]': 'true'
  }
})

export class HolidayCardComponent {


}