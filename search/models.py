from django.db import models


class Exoplanet(models.Model):
    pl_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    hostname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    default_flag = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_snum = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_pnum = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    discoverymethod = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    disc_year = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    disc_facility = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    soltype = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_controv_flag = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_refname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbper = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbpererr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbpererr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbperlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbsmax = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbsmaxerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbsmaxerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbsmaxlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_rade = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radeerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radeerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radelim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radj = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radjerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radjerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_radjlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmasse = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmasseerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmasseerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmasselim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmassj = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmassjerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmassjerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmassjlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_bmassprov = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbeccen = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbeccenerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbeccenerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_orbeccenlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_insol = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_insolerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_insolerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_insollim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_eqt = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_eqterr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_eqterr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_eqtlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    ttv_flag = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_refname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_spectype = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_teff = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_tefferr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_tefferr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_tefflim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_rad = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_raderr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_raderr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_radlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_mass = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_masserr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_masserr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_masslim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_met = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_meterr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_meterr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_metlim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_metratio = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_logg = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_loggerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_loggerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_logglim = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_refname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    rastr = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    ra = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    decstr = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    dec = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_dist = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_disterr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_disterr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_vmag = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_vmagerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_vmagerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_kmag = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_kmagerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_kmagerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_gaiamag = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_gaiamagerr1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sy_gaiamagerr2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    rowupdate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_pubdate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    releasedate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.pl_name
