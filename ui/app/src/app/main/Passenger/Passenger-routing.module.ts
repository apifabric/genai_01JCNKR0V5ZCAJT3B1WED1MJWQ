import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PassengerHomeComponent } from './home/Passenger-home.component';
import { PassengerNewComponent } from './new/Passenger-new.component';
import { PassengerDetailComponent } from './detail/Passenger-detail.component';

const routes: Routes = [
  {path: '', component: PassengerHomeComponent},
  { path: 'new', component: PassengerNewComponent },
  { path: ':id', component: PassengerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Passenger-detail-permissions'
      }
    }
  }
];

export const PASSENGER_MODULE_DECLARATIONS = [
    PassengerHomeComponent,
    PassengerNewComponent,
    PassengerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PassengerRoutingModule { }