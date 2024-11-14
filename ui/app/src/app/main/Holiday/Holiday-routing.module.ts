import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HolidayHomeComponent } from './home/Holiday-home.component';
import { HolidayNewComponent } from './new/Holiday-new.component';
import { HolidayDetailComponent } from './detail/Holiday-detail.component';

const routes: Routes = [
  {path: '', component: HolidayHomeComponent},
  { path: 'new', component: HolidayNewComponent },
  { path: ':id', component: HolidayDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Holiday-detail-permissions'
      }
    }
  },{
    path: ':holiday_id/Activity', loadChildren: () => import('../Activity/Activity.module').then(m => m.ActivityModule),
    data: {
        oPermission: {
            permissionId: 'Activity-detail-permissions'
        }
    }
}
];

export const HOLIDAY_MODULE_DECLARATIONS = [
    HolidayHomeComponent,
    HolidayNewComponent,
    HolidayDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HolidayRoutingModule { }