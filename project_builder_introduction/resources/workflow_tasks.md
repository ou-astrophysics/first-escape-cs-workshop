## Workflow Name: classify lightcurves live

### Task: T0

#### Help

1. What are **SuperWASP data**?

SuperWASP takes wide-angle images of the night sky, hundreds of times per night, and each image contains hundreds of thousands of stars.

![images](https://panoptes-uploads.zooniverse.org/production/project_attached_image/d98f6123-937e-474b-9309-8ad9b0030d7f.png)

2. What is a **lightcurve**?

The brightness of every star in every image is measured, and the measurements of each individual star are strung together to make a lightcurve - simply a sequence of brightness measurements over time. A typical SuperWASP lightcurve may contain 20,000 measurements. The SuperWASP archive contains lightcurves of more than 30 million stars.

![Lightcurve](https://panoptes-uploads.zooniverse.org/production/project_attached_image/2e324c35-2e72-4458-b8f8-177a49ff5c4b.png)

3. What is a **folded** lightcurve?

Each lightcurve in the SuperWASP archive is processed using a computer program to search for possible periodic variations in brightness. For each potential period found, the lightcurve is "folded" at that period. This means that each brightness measurement is assigned a phase in the periodic cycle. When the folded lightcurve is plotted, each brightness measurement appears at its associated phase - between 0 and 1. 

Therefore each folded lightcurve contains a series of data points - one point corresponding to each brightness measurement. A lightcurve containing a genuine periodic signal will show these data points to be distributed in a smoothly varying manner throughout the cycle. Each folded lightcurve included here is plotted repeated over **two** cycles, to help you see any variation.

![Fold](https://panoptes-uploads.zooniverse.org/production/project_attached_image/f18f492a-66f8-4465-bcfc-1986ceb41ba4.gif)

The period at which the data are folded is shown at the top of the image in equivalent values of seconds, hours and days.

4. What is the **red line** on each image?

The red line over-plotted on each image is the *average* of the folded lightcurve. In each of 100 small ranges of the cycle (known as *phase bins*), the many data points are averaged to produce a single value. This average folded lightcurve therefore indicates the average variation of brightness of the star throughout the many years of observations.

![Fold](https://panoptes-uploads.zooniverse.org/production/project_attached_image/7880bed1-2d54-4a68-8263-e79ed5fa4590.gif)

The folded lightcurves are aligned so that the minimum occurs around phase 0 of the cycle.

5a. **Pulsators**

These include RR Lyrae type, Delta Scuti type, Cepheid and Mira type stars, amongst others.

- The folded lightcurves of pulsating stars  have a single maximum per cycle. 
- Their asymmetric pulse profiles usually have a *steeper rise* in brightness and a *shallower decay*. 
- Their pulsation periods can range from a few hours to hundreds of days, for different types of pulsator.

Further examples are in the Field Guide.

![Pulsator](https://panoptes-uploads.zooniverse.org/production/project_attached_image/f3d1665b-4119-4925-ad2c-d786a30ba79d.gif)

5b. **Pulsators folded at the wrong period**

Sometimes the automated software identifies an incorrect period for a pulsating star which is genuinely periodic at some other period. 

These lightcurves will show some regular structure, but often have overlapping pulses. Such objects should be classified as pulsating stars folded at the wrong period. 

Further examples are in the Field Guide.

![Pulsator](https://panoptes-uploads.zooniverse.org/production/project_attached_image/b1b15e76-68fa-45a6-8243-5912af62554f.gif)

6a. **EA / EB type** eclipsing binaries

EA type are also known as Algol type eclipsing binaries and EB type are also known as Beta Lyrae type eclipsing binaries.

- EA and EB type eclipsing binaries both have two V-shaped minima per cycle, usually of different depths. 
- The regions between the eclipses may be relatively flat (EA) or show some variation of brightness (EB). 
- The beginning and end of eclipses are clearly defined.
- The minima are narrower than the maxima. 
- The orbital periods can range from hours to days.

Further examples are in the Field Guide.

![EA/EB](https://panoptes-uploads.zooniverse.org/production/project_attached_image/e0a2cb84-1e26-4920-860d-232c1c0554ed.gif)

It can often be difficult to distinguish between EA and EB, so they are grouped together for the purposes of classification in this project.

Sometimes the lightcurve may be folded at half the true period, so the two minima overlay one another and only one minimum is seen per cycle.  These should still be classified as EA or EB.

Further examples are in the Field Guide.

![EA/EB](https://panoptes-uploads.zooniverse.org/production/project_attached_image/400e030d-b005-4cfb-a931-8f958dda0966.gif)

6b. **EW type** eclipsing binaries

These are also known as W Ursae Majoris type eclipsing binaries.

- EW type eclipsing binaries have two minima per cycle, often of similar depths.
- They have continuously varying brightness throughout the cycle. 
- The minima are usually slightly narrower than the maxima. 
- The minima may be flat-bottomed. 
- The maxima may be different heights.
- The orbital periods are less than 1 day.

Further examples are in the Field Guide.

![EW type](https://panoptes-uploads.zooniverse.org/production/project_attached_image/39405708-8a93-4dbf-b200-0dd96d72738e.gif)

Often, these stars will be identified at *half* their true period and so only one maximum and minimum per cycle will be seen when the two minima overlay one another. These should still be classified as EW.

Further examples are in the Field Guide.

![EW type](https://panoptes-uploads.zooniverse.org/production/project_attached_image/52f4da8f-0541-4b98-aa48-c6fbfb3be89c.gif)

6c. **EA/EB/EW type folded at the wrong period**

Sometimes the automated software identifies an incorrect period for an EA, EB or EW eclipsing binary star which is genuinely periodic at some other period. 

These lightcurves will show some regular structure, but often have overlapping eclipses or multiple structures at all phases. Such objects should be classified as EA, EB or EW eclipsing binary stars folded at the wrong period. 

Further examples are in the Field Guide.

![EA/EB wrong period](https://panoptes-uploads.zooniverse.org/production/project_attached_image/0e4aa751-1d4b-4519-b540-769acacc7a65.gif)

![EW wrong period](https://panoptes-uploads.zooniverse.org/production/project_attached_image/66b0150b-25ed-416f-b50d-3f8145c48818.gif)

7. **Rotators**

Rotationally modulated stars usually have symmetric, often sinusoidal lightcurves, that vary continuously. Alternatively the folded lightcurves may look somewhat triangular in shape with symmetrical rise and fall. They have one maximum and one minimum per cycle, of equal width.

They may be due either to star spots on a single star or ellipsoidal variation in a close (non-eclipsing) binary star. Modulation periods can range from a few hours to tens of days.

Further examples are in the Field Guide.

![Rotator](https://panoptes-uploads.zooniverse.org/production/project_attached_image/9ae40460-0d6a-4433-b408-6b63e39af711.gif)

For short period rotators (periods less than a day or so), because the modulation is essentially sinusoidal, the folded lightcurve will usually look broadly the same shape if it is turned upside down. This is a useful check to distinguish such a lightcurve from that of an EW type eclipsing binary that is folded at half the true period.

For long period rotators (periods more than a few days), it can be difficult to distinguish between rotational modulation and pulsation. If the profile is *symmetrical* it is likely a rotator; if the profile is *asymmetrical* it is likely a pulsator.

8. **Unknown type**

Some stars may show a clear, periodic signal in their folded lightcurve whose shape does not match that expected of any of the named types. Such stars should be classified as unknown type periodic variables.

Further examples are in the Field Guide.

![Unknown](https://panoptes-uploads.zooniverse.org/production/project_attached_image/72aa1d96-e4ab-444d-87ff-de0d7ce152b3.gif)

9. **Junk lightcurves**

Everything else may be classified as junk! 

Often there are systematic noise effects in the data which can be mis-interpreted by the automated period search software as a periodic signal. These can be data drop-outs, noise at the start or end of an observing night, or flaring events. Some examples are shown below.

![Junk](https://panoptes-uploads.zooniverse.org/production/project_attached_image/e1721b6b-3c6c-4d24-a421-2b70a731174b.gif)

![Junk](https://panoptes-uploads.zooniverse.org/production/project_attached_image/de3da798-a52e-4617-810e-cc75bdf7f240.gif)

![Junk](https://panoptes-uploads.zooniverse.org/production/project_attached_image/19d35283-632c-4811-b286-2d5bad71fbe0.gif)

#### Type

single

#### Answers

* * label: Pulsator
  * next: T2
* label: EA/EB type
  * next: T1
* label: EW type
  * next: T1
* label: Rotator
  * next: Finish
* label: Unknown
  * next: Finish
* label: Junk
  * next: Finish


#### Question

What type of lightcurve is this?

#### Required

True

#### EnableHidePrevMarks

False

### Task: T1

#### Help

Eclipsing binary lightcurves may be:

- folded at the **correct** period such that they show two maxima / two minima per cycle; 

- folded at **half** the correct period such that they show one maximum / one minimum per cycle; 

- folded at the **wrong** period such that they show some regular structures but often have overlapping eclipses. 


#### Type

single

#### Answers

* * label: Correct period
  * next: Finish
* label: Half correct period
  * next: Finish
* label: Wrong period
  * next: Finish


#### Question

Is the eclipsing binary lightcurve folded at the correct period?

#### Required

True

### Task: T2

#### Help

Pulsating star lightcurves may be

- folded at the **correct** period such that they show one maximum / one minimum per cycle; 

- folded at the **wrong** period such that they some regular structure, but often have overlapping pulses. 

#### Type

single

#### Answers

* * label: Correct period
  * next: Finish
* label: Wrong period
  * next: Finish


#### Question

Is the pulsating star lightcurve folded at the correct period?

#### Required

True

