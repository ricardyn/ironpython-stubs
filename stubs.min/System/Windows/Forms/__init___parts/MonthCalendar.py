class MonthCalendar(Control,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent):
 """
 Represents a Windows control that enables the user to select a date using a visual monthly calendar display.
 
 MonthCalendar()
 """
 def AccessibilityNotifyClients(self,*args):
  """
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,objectID: int,childID: int)
   Notifies the accessibility client applications of the specified 
    System.Windows.Forms.AccessibleEvents for the specified child control .
  
  
   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client 
    applications of.
  
   objectID: The identifier of the System.Windows.Forms.AccessibleObject.
   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,childID: int)
   Notifies the accessibility client applications of the specified 
    System.Windows.Forms.AccessibleEvents for the specified child control.
  
  
   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client 
    applications of.
  
   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  """
  pass
 def AddAnnuallyBoldedDate(self,date):
  """
  AddAnnuallyBoldedDate(self: MonthCalendar,date: DateTime)
   Adds a day that is displayed in bold on an annual basis in the month calendar.
  
   date: The date to be displayed in bold.
  """
  pass
 def AddBoldedDate(self,date):
  """
  AddBoldedDate(self: MonthCalendar,date: DateTime)
   Adds a day to be displayed in bold in the month calendar.
  
   date: The date to be displayed in bold.
  """
  pass
 def AddMonthlyBoldedDate(self,date):
  """
  AddMonthlyBoldedDate(self: MonthCalendar,date: DateTime)
   Adds a day that is displayed in bold on a monthly basis in the month calendar.
  
   date: The date to be displayed in bold.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: Control) -> AccessibleObject
  
   Creates a new accessibility object for the control.
   Returns: A new System.Windows.Forms.AccessibleObject for the control.
  """
  pass
 def CreateControlsInstance(self,*args):
  """
  CreateControlsInstance(self: Control) -> ControlCollection
  
   Creates a new instance of the control collection for the control.
   Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to 
    the control.
  """
  pass
 def CreateHandle(self,*args):
  """
  CreateHandle(self: MonthCalendar)
   Overrides the System.Windows.Forms.Control.CreateHandle method.
  """
  pass
 def DefWndProc(self,*args):
  """ DefWndProc(self: MonthCalendar,m: Message) -> Message """
  pass
 def DestroyHandle(self,*args):
  """
  DestroyHandle(self: Control)
   Destroys the handle associated with the control.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: MonthCalendar,disposing: bool)
   Releases all resources used by the System.Windows.Forms.MonthCalendar.
  
   disposing: true to release both managed and unmanaged resources; false to release only 
    unmanaged resources.
  """
  pass
 def GetAccessibilityObjectById(self,*args):
  """
  GetAccessibilityObjectById(self: Control,objectId: int) -> AccessibleObject
  
   Retrieves the specified System.Windows.Forms.AccessibleObject.
  
   objectId: An Int32 that identifies the System.Windows.Forms.AccessibleObject to retrieve.
   Returns: An System.Windows.Forms.AccessibleObject.
  """
  pass
 def GetAutoSizeMode(self,*args):
  """
  GetAutoSizeMode(self: Control) -> AutoSizeMode
  
   Retrieves a value indicating how a control will behave when its 
    System.Windows.Forms.Control.AutoSize property is enabled.
  
   Returns: One of the System.Windows.Forms.AutoSizeMode values.
  """
  pass
 def GetDisplayRange(self,visible):
  """
  GetDisplayRange(self: MonthCalendar,visible: bool) -> SelectionRange
  
   Retrieves date information that represents the low and high limits of the 
    displayed dates of the control.
  
  
   visible: true to retrieve only the dates that are fully contained in displayed months; 
    otherwise,false.
  
   Returns: The begin and end dates of the displayed calendar.
  """
  pass
 def GetScaledBounds(self,*args):
  """
  GetScaledBounds(self: Control,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle
  
   Retrieves the bounds within which the control is scaled.
  
   bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the 
    display bounds.
  
   factor: The height and width of the control's bounds.
   specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the 
    bounds of the control to use when defining its size and position.
  
   Returns: A System.Drawing.Rectangle representing the bounds within which the control is 
    scaled.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object
  
   Returns an object that represents a service provided by the 
    System.ComponentModel.Component or by its System.ComponentModel.Container.
  
  
   service: A service provided by the System.ComponentModel.Component.
   Returns: An System.Object that represents a service provided by the 
    System.ComponentModel.Component,or null if the System.ComponentModel.Component 
    does not provide the specified service.
  """
  pass
 def GetStyle(self,*args):
  """
  GetStyle(self: Control,flag: ControlStyles) -> bool
  
   Retrieves the value of the specified control style bit for the control.
  
   flag: The System.Windows.Forms.ControlStyles bit to return the value from.
   Returns: true if the specified control style bit is set to true; otherwise,false.
  """
  pass
 def GetTopLevel(self,*args):
  """
  GetTopLevel(self: Control) -> bool
  
   Determines if the control is a top-level control.
   Returns: true if the control is a top-level control; otherwise,false.
  """
  pass
 def HitTest(self,*__args):
  """
  HitTest(self: MonthCalendar,point: Point) -> HitTestInfo
  
   Returns an object with information on which portion of a month calendar control 
    is at a location specified by a System.Drawing.Point.
  
  
   point: A System.Drawing.Point containing the System.Drawing.Point.X and 
    System.Drawing.Point.Y coordinates of the point to be hit tested.
  
   Returns: A System.Windows.Forms.MonthCalendar.HitTestInfo that contains information 
    about the specified point on the System.Windows.Forms.MonthCalendar.
  
  HitTest(self: MonthCalendar,x: int,y: int) -> HitTestInfo
  
   Returns a System.Windows.Forms.MonthCalendar.HitTestInfo with information on 
    which portion of a month calendar control is at a specified x- and 
    y-coordinate.
  
  
   x: The System.Drawing.Point.X coordinate of the point to be hit tested.
   y: The System.Drawing.Point.Y coordinate of the point to be hit tested.
   Returns: A System.Windows.Forms.MonthCalendar.HitTestInfo that contains information 
    about the specified point on the System.Windows.Forms.MonthCalendar.
  """
  pass
 def InitLayout(self,*args):
  """
  InitLayout(self: Control)
   Called after the control has been added to another container.
  """
  pass
 def InvokeGotFocus(self,*args):
  """
  InvokeGotFocus(self: Control,toInvoke: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.GotFocus event for the specified 
    control.
  
  
   toInvoke: The System.Windows.Forms.Control to assign the event to.
   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokeLostFocus(self,*args):
  """
  InvokeLostFocus(self: Control,toInvoke: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.LostFocus event for the specified 
    control.
  
  
   toInvoke: The System.Windows.Forms.Control to assign the event to.
   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokeOnClick(self,*args):
  """
  InvokeOnClick(self: Control,toInvoke: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Click event for the specified control.
  
   toInvoke: The System.Windows.Forms.Control to assign the 
    System.Windows.Forms.Control.Click event to.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokePaint(self,*args):
  """
  InvokePaint(self: Control,c: Control,e: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event for the specified control.
  
   c: The System.Windows.Forms.Control to assign the 
    System.Windows.Forms.Control.Paint event to.
  
   e: An System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def InvokePaintBackground(self,*args):
  """
  InvokePaintBackground(self: Control,c: Control,e: PaintEventArgs)
   Raises the PaintBackground event for the specified control.
  
   c: The System.Windows.Forms.Control to assign the 
    System.Windows.Forms.Control.Paint event to.
  
   e: An System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def IsInputChar(self,*args):
  """
  IsInputChar(self: Control,charCode: Char) -> bool
  
   Determines if a character is an input character that the control recognizes.
  
   charCode: The character to test.
   Returns: true if the character should be sent directly to the control and not 
    preprocessed; otherwise,false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: MonthCalendar,keyData: Keys) -> bool
  
   keyData: One of the System.Windows.Forms.Keys values.
   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which 
    will cause the object to be assigned a new identity when it is marshaled across 
    a remoting boundary. A value of false is usually appropriate. true to copy the 
    current System.MarshalByRefObject object's identity to its clone,which will 
    cause remoting client calls to be routed to the remote server object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def NotifyInvalidate(self,*args):
  """
  NotifyInvalidate(self: Control,invalidatedArea: Rectangle)
   Raises the System.Windows.Forms.Control.Invalidated event with a specified 
    region of the control to invalidate.
  
  
   invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
  """
  pass
 def OnAutoSizeChanged(self,*args):
  """
  OnAutoSizeChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.AutoSizeChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: MonthCalendar,e: EventArgs)
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundImageChanged(self,*args):
  """
  OnBackgroundImageChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BackgroundImageChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundImageLayoutChanged(self,*args):
  """
  OnBackgroundImageLayoutChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BackgroundImageLayoutChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBindingContextChanged(self,*args):
  """
  OnBindingContextChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BindingContextChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCausesValidationChanged(self,*args):
  """
  OnCausesValidationChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.CausesValidationChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnChangeUICues(self,*args):
  """
  OnChangeUICues(self: Control,e: UICuesEventArgs)
   Raises the System.Windows.Forms.Control.ChangeUICues event.
  
   e: A System.Windows.Forms.UICuesEventArgs that contains the event data.
  """
  pass
 def OnClick(self,*args):
  """
  OnClick(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Click event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnClientSizeChanged(self,*args):
  """
  OnClientSizeChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ClientSizeChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnContextMenuChanged(self,*args):
  """
  OnContextMenuChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ContextMenuChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnContextMenuStripChanged(self,*args):
  """
  OnContextMenuStripChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ContextMenuStripChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnControlAdded(self,*args):
  """
  OnControlAdded(self: Control,e: ControlEventArgs)
   Raises the System.Windows.Forms.Control.ControlAdded event.
  
   e: A System.Windows.Forms.ControlEventArgs that contains the event data.
  """
  pass
 def OnControlRemoved(self,*args):
  """
  OnControlRemoved(self: Control,e: ControlEventArgs)
   Raises the System.Windows.Forms.Control.ControlRemoved event.
  
   e: A System.Windows.Forms.ControlEventArgs that contains the event data.
  """
  pass
 def OnCreateControl(self,*args):
  """
  OnCreateControl(self: Control)
   Raises the System.Windows.Forms.Control.CreateControl method.
  """
  pass
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.CursorChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDateChanged(self,*args):
  """
  OnDateChanged(self: MonthCalendar,drevent: DateRangeEventArgs)
   Raises the System.Windows.Forms.MonthCalendar.DateChanged event.
  
   drevent: A System.Windows.Forms.DateRangeEventArgs that contains the event data.
  """
  pass
 def OnDateSelected(self,*args):
  """
  OnDateSelected(self: MonthCalendar,drevent: DateRangeEventArgs)
   Raises the System.Windows.Forms.MonthCalendar.DateSelected event.
  
   drevent: A System.Windows.Forms.DateRangeEventArgs that contains the event data.
  """
  pass
 def OnDockChanged(self,*args):
  """
  OnDockChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.DockChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDoubleClick(self,*args):
  """
  OnDoubleClick(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.DoubleClick event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDragDrop(self,*args):
  """
  OnDragDrop(self: Control,drgevent: DragEventArgs)
   Raises the System.Windows.Forms.Control.DragDrop event.
  
   drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: Control,drgevent: DragEventArgs)
   Raises the System.Windows.Forms.Control.DragEnter event.
  
   drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.DragLeave event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: Control,drgevent: DragEventArgs)
   Raises the System.Windows.Forms.Control.DragOver event.
  
   drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnEnabledChanged(self,*args):
  """
  OnEnabledChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.EnabledChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEnter(self,*args):
  """
  OnEnter(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Enter event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: MonthCalendar,e: EventArgs)
   Raises the System.Windows.Forms.Control.FontChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: MonthCalendar,e: EventArgs)
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: Control,gfbevent: GiveFeedbackEventArgs)
   Raises the System.Windows.Forms.Control.GiveFeedback event.
  
   gfbevent: A System.Windows.Forms.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.GotFocus event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleCreated(self,*args):
  """
  OnHandleCreated(self: MonthCalendar,e: EventArgs)
   Overrides the System.Windows.Forms.Control.OnHandleCreated(System.EventArgs) 
    method.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: MonthCalendar,e: EventArgs)
   Raises the System.Windows.Forms.Control.HandleDestroyed event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHelpRequested(self,*args):
  """
  OnHelpRequested(self: Control,hevent: HelpEventArgs)
   Raises the System.Windows.Forms.Control.HelpRequested event.
  
   hevent: A System.Windows.Forms.HelpEventArgs that contains the event data.
  """
  pass
 def OnImeModeChanged(self,*args):
  """
  OnImeModeChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ImeModeChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnInvalidated(self,*args):
  """
  OnInvalidated(self: Control,e: InvalidateEventArgs)
   Raises the System.Windows.Forms.Control.Invalidated event.
  
   e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: Control,e: KeyEventArgs)
   Raises the System.Windows.Forms.Control.KeyDown event.
  
   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: Control,e: KeyPressEventArgs)
   Raises the System.Windows.Forms.Control.KeyPress event.
  
   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: Control,e: KeyEventArgs)
   Raises the System.Windows.Forms.Control.KeyUp event.
  
   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnLayout(self,*args):
  """
  OnLayout(self: Control,levent: LayoutEventArgs)
   Raises the System.Windows.Forms.Control.Layout event.
  
   levent: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Leave event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLocationChanged(self,*args):
  """
  OnLocationChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.LocationChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.LostFocus event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMarginChanged(self,*args):
  """
  OnMarginChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.MarginChanged event.
  
   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnMouseCaptureChanged(self,*args):
  """
  OnMouseCaptureChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.MouseCaptureChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseClick(self,*args):
  """
  OnMouseClick(self: Control,e: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseClick event.
  
   e: An System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: Control,e: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseDoubleClick event.
  
   e: An System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: Control,e: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseDown event.
  
   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.MouseEnter event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseHover(self,*args):
  """
  OnMouseHover(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.MouseHover event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.MouseLeave event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: Control,e: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseMove event.
  
   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: Control,e: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseUp event.
  
   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: Control,e: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseWheel event.
  
   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMove(self,*args):
  """
  OnMove(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Move event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnNotifyMessage(self,*args):
  """
  OnNotifyMessage(self: Control,m: Message)
   Notifies the control of Windows messages.
  
   m: A System.Windows.Forms.Message that represents the Windows message.
  """
  pass
 def OnPaddingChanged(self,*args):
  """
  OnPaddingChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.PaddingChanged event.
  
   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnPaint(self,*args):
  """
  OnPaint(self: Control,e: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event.
  
   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnPaintBackground(self,*args):
  """
  OnPaintBackground(self: Control,pevent: PaintEventArgs)
   Paints the background of the control.
  
   pevent: A System.Windows.Forms.PaintEventArgs that contains information about the 
    control to paint.
  """
  pass
 def OnParentBackColorChanged(self,*args):
  """
  OnParentBackColorChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BackColorChanged event when the 
    System.Windows.Forms.Control.BackColor property value of the control's 
    container changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBackgroundImageChanged(self,*args):
  """
  OnParentBackgroundImageChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the 
    System.Windows.Forms.Control.BackgroundImage property value of the control's 
    container changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBindingContextChanged(self,*args):
  """
  OnParentBindingContextChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BindingContextChanged event when the 
    System.Windows.Forms.Control.BindingContext property value of the control's 
    container changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentChanged(self,*args):
  """
  OnParentChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ParentChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentCursorChanged(self,*args):
  """
  OnParentCursorChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.CursorChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentEnabledChanged(self,*args):
  """
  OnParentEnabledChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.EnabledChanged event when the 
    System.Windows.Forms.Control.Enabled property value of the control's container 
    changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentFontChanged(self,*args):
  """
  OnParentFontChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.FontChanged event when the 
    System.Windows.Forms.Control.Font property value of the control's container 
    changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentForeColorChanged(self,*args):
  """
  OnParentForeColorChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ForeColorChanged event when the 
    System.Windows.Forms.Control.ForeColor property value of the control's 
    container changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentRightToLeftChanged(self,*args):
  """
  OnParentRightToLeftChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.RightToLeftChanged event when the 
    System.Windows.Forms.Control.RightToLeft property value of the control's 
    container changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentVisibleChanged(self,*args):
  """
  OnParentVisibleChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.VisibleChanged event when the 
    System.Windows.Forms.Control.Visible property value of the control's container 
    changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: Control,e: PreviewKeyDownEventArgs)
   Raises the System.Windows.Forms.Control.PreviewKeyDown event.
  
   e: A System.Windows.Forms.PreviewKeyDownEventArgs that contains the event data.
  """
  pass
 def OnPrint(self,*args):
  """
  OnPrint(self: Control,e: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event.
  
   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: Control,qcdevent: QueryContinueDragEventArgs)
   Raises the System.Windows.Forms.Control.QueryContinueDrag event.
  
   qcdevent: A System.Windows.Forms.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnRegionChanged(self,*args):
  """
  OnRegionChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.RegionChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnResize(self,*args):
  """
  OnResize(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Resize event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.RightToLeftChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftLayoutChanged(self,*args):
  """
  OnRightToLeftLayoutChanged(self: MonthCalendar,e: EventArgs)
   Raises the System.Windows.Forms.MonthCalendar.RightToLeftLayoutChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSizeChanged(self,*args):
  """
  OnSizeChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.SizeChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnStyleChanged(self,*args):
  """
  OnStyleChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.StyleChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSystemColorsChanged(self,*args):
  """
  OnSystemColorsChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.SystemColorsChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTabIndexChanged(self,*args):
  """
  OnTabIndexChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.TabIndexChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTabStopChanged(self,*args):
  """
  OnTabStopChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.TabStopChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTextChanged(self,*args):
  """
  OnTextChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.TextChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnValidated(self,*args):
  """
  OnValidated(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Validated event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnValidating(self,*args):
  """
  OnValidating(self: Control,e: CancelEventArgs)
   Raises the System.Windows.Forms.Control.Validating event.
  
   e: A System.ComponentModel.CancelEventArgs that contains the event data.
  """
  pass
 def OnVisibleChanged(self,*args):
  """
  OnVisibleChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.VisibleChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: Control,msg: Message,keyData: Keys) -> (bool,Message)
  
   Processes a command key.
  
   msg: A System.Windows.Forms.Message,passed by reference,that represents the window 
    message to process.
  
   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogChar(self,*args):
  """
  ProcessDialogChar(self: Control,charCode: Char) -> bool
  
   Processes a dialog character.
  
   charCode: The character to process.
   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: Control,keyData: Keys) -> bool
  
   Processes a dialog key.
  
   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
   Returns: true if the key was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyEventArgs(self,*args):
  """
  ProcessKeyEventArgs(self: Control,m: Message) -> (bool,Message)
  
   Processes a key message and generates the appropriate control events.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window 
    message to process.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyMessage(self,*args):
  """
  ProcessKeyMessage(self: Control,m: Message) -> (bool,Message)
  
   Processes a keyboard message.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window 
    message to process.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyPreview(self,*args):
  """
  ProcessKeyPreview(self: Control,m: Message) -> (bool,Message)
  
   Previews a keyboard message.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window 
    message to process.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: Control,charCode: Char) -> bool
  
   Processes a mnemonic character.
  
   charCode: The character to process.
   Returns: true if the character was processed as a mnemonic by the control; otherwise,
    false.
  """
  pass
 def RaiseDragEvent(self,*args):
  """
  RaiseDragEvent(self: Control,key: object,e: DragEventArgs)
   Raises the appropriate drag event.
  
   key: The event to raise.
   e: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def RaiseKeyEvent(self,*args):
  """
  RaiseKeyEvent(self: Control,key: object,e: KeyEventArgs)
   Raises the appropriate key event.
  
   key: The event to raise.
   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def RaiseMouseEvent(self,*args):
  """
  RaiseMouseEvent(self: Control,key: object,e: MouseEventArgs)
   Raises the appropriate mouse event.
  
   key: The event to raise.
   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def RaisePaintEvent(self,*args):
  """
  RaisePaintEvent(self: Control,key: object,e: PaintEventArgs)
   Raises the appropriate paint event.
  
   key: The event to raise.
   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def RecreateHandle(self,*args):
  """
  RecreateHandle(self: Control)
   Forces the re-creation of the handle for the control.
  """
  pass
 def RemoveAllAnnuallyBoldedDates(self):
  """
  RemoveAllAnnuallyBoldedDates(self: MonthCalendar)
   Removes all the annually bold dates.
  """
  pass
 def RemoveAllBoldedDates(self):
  """
  RemoveAllBoldedDates(self: MonthCalendar)
   Removes all the nonrecurring bold dates.
  """
  pass
 def RemoveAllMonthlyBoldedDates(self):
  """
  RemoveAllMonthlyBoldedDates(self: MonthCalendar)
   Removes all the monthly bold dates.
  """
  pass
 def RemoveAnnuallyBoldedDate(self,date):
  """
  RemoveAnnuallyBoldedDate(self: MonthCalendar,date: DateTime)
   Removes the specified date from the list of annually bold dates.
  
   date: The date to remove from the date list.
  """
  pass
 def RemoveBoldedDate(self,date):
  """
  RemoveBoldedDate(self: MonthCalendar,date: DateTime)
   Removes the specified date from the list of nonrecurring bold dates.
  
   date: The date to remove from the date list.
  """
  pass
 def RemoveMonthlyBoldedDate(self,date):
  """
  RemoveMonthlyBoldedDate(self: MonthCalendar,date: DateTime)
   Removes the specified date from the list of monthly bolded dates.
  
   date: The date to remove from the date list.
  """
  pass
 def ResetMouseEventArgs(self,*args):
  """
  ResetMouseEventArgs(self: Control)
   Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
  """
  pass
 def RtlTranslateAlignment(self,*args):
  """
  RtlTranslateAlignment(self: Control,align: ContentAlignment) -> ContentAlignment
  
   Converts the specified System.Drawing.ContentAlignment to the appropriate 
    System.Drawing.ContentAlignment to support right-to-left text.
  
  
   align: One of the System.Drawing.ContentAlignment values.
   Returns: One of the System.Drawing.ContentAlignment values.
  RtlTranslateAlignment(self: Control,align: LeftRightAlignment) -> LeftRightAlignment
  
   Converts the specified System.Windows.Forms.LeftRightAlignment to the 
    appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left 
    text.
  
  
   align: One of the System.Windows.Forms.LeftRightAlignment values.
   Returns: One of the System.Windows.Forms.LeftRightAlignment values.
  RtlTranslateAlignment(self: Control,align: HorizontalAlignment) -> HorizontalAlignment
  
   Converts the specified System.Windows.Forms.HorizontalAlignment to the 
    appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left 
    text.
  
  
   align: One of the System.Windows.Forms.HorizontalAlignment values.
   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  """
  pass
 def RtlTranslateContent(self,*args):
  """
  RtlTranslateContent(self: Control,align: ContentAlignment) -> ContentAlignment
  
   Converts the specified System.Drawing.ContentAlignment to the appropriate 
    System.Drawing.ContentAlignment to support right-to-left text.
  
  
   align: One of the System.Drawing.ContentAlignment values.
   Returns: One of the System.Drawing.ContentAlignment values.
  """
  pass
 def RtlTranslateHorizontal(self,*args):
  """
  RtlTranslateHorizontal(self: Control,align: HorizontalAlignment) -> HorizontalAlignment
  
   Converts the specified System.Windows.Forms.HorizontalAlignment to the 
    appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left 
    text.
  
  
   align: One of the System.Windows.Forms.HorizontalAlignment values.
   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  """
  pass
 def RtlTranslateLeftRight(self,*args):
  """
  RtlTranslateLeftRight(self: Control,align: LeftRightAlignment) -> LeftRightAlignment
  
   Converts the specified System.Windows.Forms.LeftRightAlignment to the 
    appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left 
    text.
  
  
   align: One of the System.Windows.Forms.LeftRightAlignment values.
   Returns: One of the System.Windows.Forms.LeftRightAlignment values.
  """
  pass
 def ScaleControl(self,*args):
  """
  ScaleControl(self: Control,factor: SizeF,specified: BoundsSpecified)
   Scales a control's location,size,padding and margin.
  
   factor: The factor by which the height and width of the control will be scaled.
   specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the 
    control to use when defining its size and position.
  """
  pass
 def ScaleCore(self,*args):
  """
  ScaleCore(self: Control,dx: Single,dy: Single)
   This method is not relevant for this class.
  
   dx: The horizontal scaling factor.
   dy: The vertical scaling factor.
  """
  pass
 def Select(self):
  """
  Select(self: Control,directed: bool,forward: bool)
   Activates a child control. Optionally specifies the direction in the tab order 
    to select the control from.
  
  
   directed: true to specify the direction of the control to select; otherwise,false.
   forward: true to move forward in the tab order; false to move backward in the tab order.
  """
  pass
 def SetAutoSizeMode(self,*args):
  """
  SetAutoSizeMode(self: Control,mode: AutoSizeMode)
   Sets a value indicating how a control will behave when its 
    System.Windows.Forms.Control.AutoSize property is enabled.
  
  
   mode: One of the System.Windows.Forms.AutoSizeMode values.
  """
  pass
 def SetBoundsCore(self,*args):
  """
  SetBoundsCore(self: MonthCalendar,x: int,y: int,width: int,height: int,specified: BoundsSpecified)
   Overrides the 
    System.Windows.Forms.Control.SetBoundsCore(System.Int32,System.Int32,System.Int3
    2,System.Int32,System.Windows.Forms.BoundsSpecified) method.
  
  
   x: The new System.Windows.Forms.Control.Left property value of the control.
   y: The new System.Windows.Forms.Control.Right property value of the control.
   width: The new System.Windows.Forms.Control.Width property value of the control.
   height: The new System.Windows.Forms.Control.Height property value of the control.
   specified: A bitwise combination of the System.Windows.Forms.BoundsSpecified values.
  """
  pass
 def SetCalendarDimensions(self,x,y):
  """
  SetCalendarDimensions(self: MonthCalendar,x: int,y: int)
   Sets the number of columns and rows of months to display.
  
   x: The number of columns.
   y: The number of rows.
  """
  pass
 def SetClientSizeCore(self,*args):
  """
  SetClientSizeCore(self: Control,x: int,y: int)
   Sets the size of the client area of the control.
  
   x: The client area width,in pixels.
   y: The client area height,in pixels.
  """
  pass
 def SetDate(self,date):
  """
  SetDate(self: MonthCalendar,date: DateTime)
   Sets a date as the currently selected date.
  
   date: The date to be selected.
  """
  pass
 def SetSelectionRange(self,date1,date2):
  """
  SetSelectionRange(self: MonthCalendar,date1: DateTime,date2: DateTime)
   Sets the selected dates in a month calendar control to the specified date range.
  
   date1: The beginning date of the selection range.
   date2: The end date of the selection range.
  """
  pass
 def SetStyle(self,*args):
  """
  SetStyle(self: Control,flag: ControlStyles,value: bool)
   Sets a specified System.Windows.Forms.ControlStyles flag to either true or 
    false.
  
  
   flag: The System.Windows.Forms.ControlStyles bit to set.
   value: true to apply the specified style to the control; otherwise,false.
  """
  pass
 def SetTopLevel(self,*args):
  """
  SetTopLevel(self: Control,value: bool)
   Sets the control as the top-level control.
  
   value: true to set the control as the top-level control; otherwise,false.
  """
  pass
 def SetVisibleCore(self,*args):
  """
  SetVisibleCore(self: Control,value: bool)
   Sets the control to the specified visible state.
  
   value: true to make the control visible; otherwise,false.
  """
  pass
 def SizeFromClientSize(self,*args):
  """
  SizeFromClientSize(self: Control,clientSize: Size) -> Size
  
   Determines the size of the entire control from the height and width of its 
    client area.
  
  
   clientSize: A System.Drawing.Size value representing the height and width of the control's 
    client area.
  
   Returns: A System.Drawing.Size value representing the height and width of the entire 
    control.
  """
  pass
 def ToString(self):
  """
  ToString(self: MonthCalendar) -> str
  
   Returns a string that represents the System.Windows.Forms.MonthCalendar control.
   Returns: A string that represents the current System.Windows.Forms.MonthCalendar.
  """
  pass
 def UpdateBoldedDates(self):
  """
  UpdateBoldedDates(self: MonthCalendar)
   Repaints the bold dates to reflect the dates set in the lists of bold dates.
  """
  pass
 def UpdateBounds(self,*args):
  """
  UpdateBounds(self: Control,x: int,y: int,width: int,height: int,clientWidth: int,clientHeight: int)
   Updates the bounds of the control with the specified size,location,and client 
    size.
  
  
   x: The System.Drawing.Point.X coordinate of the control.
   y: The System.Drawing.Point.Y coordinate of the control.
   width: The System.Drawing.Size.Width of the control.
   height: The System.Drawing.Size.Height of the control.
   clientWidth: The client System.Drawing.Size.Width of the control.
   clientHeight: The client System.Drawing.Size.Height of the control.
  UpdateBounds(self: Control,x: int,y: int,width: int,height: int)
   Updates the bounds of the control with the specified size and location.
  
   x: The System.Drawing.Point.X coordinate of the control.
   y: The System.Drawing.Point.Y coordinate of the control.
   width: The System.Drawing.Size.Width of the control.
   height: The System.Drawing.Size.Height of the control.
  UpdateBounds(self: Control)
   Updates the bounds of the control with the current size and location.
  """
  pass
 def UpdateStyles(self,*args):
  """
  UpdateStyles(self: Control)
   Forces the assigned styles to be reapplied to the control.
  """
  pass
 def UpdateZOrder(self,*args):
  """
  UpdateZOrder(self: Control)
   Updates the control in its parent's z-order.
  """
  pass
 def WndProc(self,*args):
  """
  WndProc(self: MonthCalendar,m: Message) -> Message
  
   Overrides the 
    System.Windows.Forms.Control.WndProc(System.Windows.Forms.Message@) method.
  
  
   m: The Windows System.Windows.Forms.Message to process.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 AnnuallyBoldedDates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the array of System.DateTime objects that determines which annual days are displayed in bold.

Get: AnnuallyBoldedDates(self: MonthCalendar) -> Array[DateTime]

Set: AnnuallyBoldedDates(self: MonthCalendar)=value
"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the control.

Get: BackColor(self: MonthCalendar) -> Color

Set: BackColor(self: MonthCalendar)=value
"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image for the System.Windows.Forms.MonthCalendar

Get: BackgroundImage(self: MonthCalendar) -> Image

Set: BackgroundImage(self: MonthCalendar)=value
"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the layout for the System.Windows.Forms.MonthCalendar.BackgroundImage.

Get: BackgroundImageLayout(self: MonthCalendar) -> ImageLayout

Set: BackgroundImageLayout(self: MonthCalendar)=value
"""

 BoldedDates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the array of System.DateTime objects that determines which nonrecurring dates are displayed in bold.

Get: BoldedDates(self: MonthCalendar) -> Array[DateTime]

Set: BoldedDates(self: MonthCalendar)=value
"""

 CalendarDimensions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of columns and rows of months displayed.

Get: CalendarDimensions(self: MonthCalendar) -> Size

Set: CalendarDimensions(self: MonthCalendar)=value
"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.

"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Windows.Forms.CreateParams for creating a System.Windows.Forms.MonthCalendar control.

"""

 DefaultCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default cursor for the control.

"""

 DefaultImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the input method editor for the System.Windows.Forms.MonthCalendar.

"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default margin settings for the System.Windows.Forms.MonthCalendar control.

"""

 DefaultMaximumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length and height,in pixels,that is specified as the default maximum size of a control.

"""

 DefaultMinimumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length and height,in pixels,that is specified as the default minimum size of a control.

"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing,in pixels,of the contents of a control.

"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default size of the calendar.

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control should redraw its surface using a secondary buffer.

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 FirstDayOfWeek=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the first day of the week as displayed in the month calendar.

Get: FirstDayOfWeek(self: MonthCalendar) -> Day

Set: FirstDayOfWeek(self: MonthCalendar)=value
"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the control.

Get: ForeColor(self: MonthCalendar) -> Color

Set: ForeColor(self: MonthCalendar)=value
"""

 ImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Input Method Editor (IME) mode supported by this control.

Get: ImeMode(self: MonthCalendar) -> ImeMode

Set: ImeMode(self: MonthCalendar)=value
"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.

"""

 MaxDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowable date.

Get: MaxDate(self: MonthCalendar) -> DateTime

Set: MaxDate(self: MonthCalendar)=value
"""

 MaxSelectionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of days that can be selected in a month calendar control.

Get: MaxSelectionCount(self: MonthCalendar) -> int

Set: MaxSelectionCount(self: MonthCalendar)=value
"""

 MinDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum allowable date.

Get: MinDate(self: MonthCalendar) -> DateTime

Set: MinDate(self: MonthCalendar)=value
"""

 MonthlyBoldedDates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the array of System.DateTime objects that determine which monthly days to bold.

Get: MonthlyBoldedDates(self: MonthCalendar) -> Array[DateTime]

Set: MonthlyBoldedDates(self: MonthCalendar)=value
"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between the edges of a System.Windows.Forms.MonthCalendar control and its contents.

Get: Padding(self: MonthCalendar) -> Padding

Set: Padding(self: MonthCalendar)=value
"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.

"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.

"""

 RightToLeftLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control is laid out from right to left.

Get: RightToLeftLayout(self: MonthCalendar) -> bool

Set: RightToLeftLayout(self: MonthCalendar)=value
"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.

"""

 ScrollChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scroll rate for a month calendar control.

Get: ScrollChange(self: MonthCalendar) -> int

Set: ScrollChange(self: MonthCalendar)=value
"""

 SelectionEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the end date of the selected range of dates.

Get: SelectionEnd(self: MonthCalendar) -> DateTime

Set: SelectionEnd(self: MonthCalendar)=value
"""

 SelectionRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the selected range of dates for a month calendar control.

Get: SelectionRange(self: MonthCalendar) -> SelectionRange

Set: SelectionRange(self: MonthCalendar)=value
"""

 SelectionStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the start date of the selected range of dates.

Get: SelectionStart(self: MonthCalendar) -> DateTime

Set: SelectionStart(self: MonthCalendar)=value
"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

 ShowToday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the date represented by the System.Windows.Forms.MonthCalendar.TodayDate property is displayed at the bottom of the control.

Get: ShowToday(self: MonthCalendar) -> bool

Set: ShowToday(self: MonthCalendar)=value
"""

 ShowTodayCircle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether today's date is identified with a circle or a square.

Get: ShowTodayCircle(self: MonthCalendar) -> bool

Set: ShowTodayCircle(self: MonthCalendar)=value
"""

 ShowWeekNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the month calendar control displays week numbers (1-52) to the left of each row of days.

Get: ShowWeekNumbers(self: MonthCalendar) -> bool

Set: ShowWeekNumbers(self: MonthCalendar)=value
"""

 SingleMonthSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minimum size to display one month of the calendar.

Get: SingleMonthSize(self: MonthCalendar) -> Size

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the System.Windows.Forms.MonthCalendar control.

Get: Size(self: MonthCalendar) -> Size

Set: Size(self: MonthCalendar)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text to display on the System.Windows.Forms.MonthCalendar.

Get: Text(self: MonthCalendar) -> str

Set: Text(self: MonthCalendar)=value
"""

 TitleBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the background color of the title area of the calendar.

Get: TitleBackColor(self: MonthCalendar) -> Color

Set: TitleBackColor(self: MonthCalendar)=value
"""

 TitleForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the foreground color of the title area of the calendar.

Get: TitleForeColor(self: MonthCalendar) -> Color

Set: TitleForeColor(self: MonthCalendar)=value
"""

 TodayDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value that is used by System.Windows.Forms.MonthCalendar as today's date.

Get: TodayDate(self: MonthCalendar) -> DateTime

Set: TodayDate(self: MonthCalendar)=value
"""

 TodayDateSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.MonthCalendar.TodayDate property has been explicitly set.

Get: TodayDateSet(self: MonthCalendar) -> bool

"""

 TrailingForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the color of days in months that are not fully displayed in the control.

Get: TrailingForeColor(self: MonthCalendar) -> Color

Set: TrailingForeColor(self: MonthCalendar)=value
"""


 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 Click=None
 DateChanged=None
 DateSelected=None
 DoubleClick=None
 HitArea=None
 HitTestInfo=None
 ImeModeChanged=None
 MouseClick=None
 MouseDoubleClick=None
 PaddingChanged=None
 Paint=None
 RightToLeftLayoutChanged=None
 TextChanged=None

