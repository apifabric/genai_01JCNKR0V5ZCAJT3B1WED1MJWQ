import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookingHomeComponent } from './home/Booking-home.component';
import { BookingNewComponent } from './new/Booking-new.component';
import { BookingDetailComponent } from './detail/Booking-detail.component';

const routes: Routes = [
  {path: '', component: BookingHomeComponent},
  { path: 'new', component: BookingNewComponent },
  { path: ':id', component: BookingDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Booking-detail-permissions'
      }
    }
  },{
    path: ':booking_id/Passenger', loadChildren: () => import('../Passenger/Passenger.module').then(m => m.PassengerModule),
    data: {
        oPermission: {
            permissionId: 'Passenger-detail-permissions'
        }
    }
}
];

export const BOOKING_MODULE_DECLARATIONS = [
    BookingHomeComponent,
    BookingNewComponent,
    BookingDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BookingRoutingModule { }