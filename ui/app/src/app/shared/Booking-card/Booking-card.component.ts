import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Booking-card.component.html',
  styleUrls: ['./Booking-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Booking-card]': 'true'
  }
})

export class BookingCardComponent {


}